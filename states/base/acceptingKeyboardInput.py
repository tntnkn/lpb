from keyboards          import keyboardMaker, multiPageKeyboardMaker
from .stateInterface    import stateInterface
from utils              import send_unsolicited_message
import bot

from aiogram.types import ParseMode


class acceptingKeyboardInput(stateInterface):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev)
        self.next               = None
        self.keyboard_mes_id    = keyboard_mes_id
        self.resize_keyboard    = True

    async def go(self, callback_data=None, new_user_info=None, *args, **kwargs):
        self = await super().go(callback_data, new_user_info, *args, **kwargs)
        switched, ret = await self.switch(callback_data)
        if not switched:
            ret = await self.doGo(callback_data, new_user_info)
            if callback_data != 'changing':
                self.last_callback_data = callback_data
        return ret 

    async def finish(self):
        await self.handleExistingKeyboard()
        return self

    async def switch(self, predicate=None):
        if   predicate == 'prev':
            return ( True, await self.go_prev() )
        elif predicate == 'next':
            return ( True, await self.go_next() )
        elif predicate == 'done':
            return ( True, await self.done() )
        return await self.doSwitch(predicate)

    # ---- INTERFACE SPECIFIC TO THIS STATE

    async def presentKeyboard(self, page_descr, menu_page):
        await self.handleExistingKeyboard()
        ret = await bot.bot.send_message(
            self.context.from_id, page_descr, 
            reply_markup=menu_page, parse_mode=ParseMode.HTML)
        self.keyboard_mes_id = ret["message_id"]

    async def handleExistingKeyboard(self):
        if self.keyboard_mes_id:
            await bot.bot.delete_message(
                chat_id     = self.context.from_id,
                message_id  = self.keyboard_mes_id)
            self.keyboard_mes_id = None

    def makeKeyboard(self):
        page_options    = self.getPageOptions() 
        page_descr      = self.getPageDescription() 
        menu_page       = keyboardMaker.makeKeyboard(page_options)
        return page_descr, menu_page

    def getPageDescription(self):
        return "Base menu"

    def getPageOptions(self):
        return list()

    async def doGo(self, callback_data, new_user_info):
        page_descr, menu_page = self.makeKeyboard()
        await self.presentKeyboard(page_descr, menu_page)
        return self

    async def doSwitch(self, predicate):
        return (False, self)


class acceptingWrappedKeyboardInput(acceptingKeyboardInput):
    def __init__(self, context, prev=None, keyboard_mes_id=None):
        super().__init__(context, prev, keyboard_mes_id)
        self.page_pos   = None
        self.nexts      = list()
        self.can_be_done = False

    # ---- INTERFACE SPECIFIC TO THIS STATE

    def makeKeyboard(self):
        page_descr, menu_page = super().makeKeyboard()
        page_pos  = self.getPagePos()
        menu_page = multiPageKeyboardMaker.wrapKeyboard(menu_page, page_pos)
        return page_descr, menu_page

    def getPageDescription(self):
        return "Base multi page menu"

    def getPagePos(self):
        ret = multiPageKeyboardMaker.position.NONE 
        can_go_next = self.next is not None
        can_go_prev = self.prev is not None
        can_go_both = can_go_next and can_go_prev
        can_be_done = self.can_be_done 

        if can_go_next and can_be_done:
            ret |= multiPageKeyboardMaker.position.DONE
            can_go_both = False
        if can_go_both:
            ret |= multiPageKeyboardMaker.position.MIDDLE
            can_go_next = False
            can_go_prev = False
        if can_go_next and not can_be_done:
            ret |= multiPageKeyboardMaker.position.CAN_GO_NEXT
        if can_go_prev:
            ret |= multiPageKeyboardMaker.position.CAN_GO_BACK

        return ret


class acceptingFormFillingInput(acceptingWrappedKeyboardInput):
    def __init__(self, context, prev=None, keyboard_mes_id=None, 
                 require_user_to_complete_page=True):
        super().__init__(context, prev, keyboard_mes_id)
        self.current_state  = None
        self.from_id        = context.from_id
        self.fields         = None
        self.require_user_to_complete_page = require_user_to_complete_page

    async def finish(self):
        if self.current_state:
            await self.current_state.done()
        return await super().finish()

    # ---- INTERFACE SPECIFIC TO THIS STATE

    async def doGo(self, callback_data, new_user_info=None):
        if   callback_data is None:
            return await super().doGo(callback_data, new_user_info)
        elif callback_data == "changing" and self.current_state:
            self.current_state = await self.current_state.go(new_user_info)
            if self.current_state is None:
                self.markFieldAsFilled()
                return await self.doGo(None)
        elif callback_data != "changing":
            self.setCorrectionPrompt(callback_data)
            await self.current_state.go()
        else:
            await send_unsolicited_message(
                self.context.from_id, "Сначала выберете поле в меню, которое нужно заполнить, пожалуйста.")
        return self

    def getPagePos(self):
        if self.require_user_to_complete_page and not self.checkIfPageIsFilled():
            if self.prev is not None: 
                return multiPageKeyboardMaker.position.CAN_GO_BACK
            else:
                return multiPageKeyboardMaker.position.NONE
        return super().getPagePos()

    def setCorrectionPrompt(self, callback_data):
        self.current_state = self.fields[callback_data].state(self.context)
        self.doSetCorrectionPrompt(callback_data)

    def markFieldAsFilled(self):
        self.fields[self.last_callback_data].filled = True

    def checkIfPageIsFilled(self):
        for field in self.fields.values():
            if not field.filled:
                return False
        return True

