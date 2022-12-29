from .stateInterface import stateInterface
import bot

from aiogram.types import ParseMode

class acceptingTextInput(stateInterface):
    def __init__(self, context, prev=None, message_id=None):
        super().__init__(context, prev)
        self.next               = None
        self.message_id         = message_id
        self.data_prompt        = "Тестовый промпт!"
        self.correction_prompt  = "Неправильный ввод!"

    async def go(self, thingToWrite=None, *args, **kwargs):
        self = await super().go(thingToWrite, *args, **kwargs)
        ret = None
        if thingToWrite is None:
            await self.promptForData()
            ret = self
        else:
            ret = await self.doGo(thingToWrite)
        return ret

    async def finish(self):
        await self.handleExistingMessage()
        return self

    async def switch(self, predicate=None):
        return await self.go_next()
    
    # ---- INTERFACE SPECIFIC TO THIS STATE

    async def handleExistingMessage(self):
        if self.message_id:
            await bot.bot.delete_message(
                chat_id     = self.context.from_id,
                message_id  = self.message_id)
            self.message_id = None

    async def promptForData(self):
        await self.handleExistingMessage()
        ret = await self.doPromptForData()
        self.message_id = ret["message_id"]

    async def promptForCorrection(self):
        await self.handleExistingMessage()
        ret = await self.doPromptForCorrection()
        self.message_id = ret["message_id"]

    async def checkInput(self, inp):
        return await self.doCheckInput(inp)

    async def saveInput(self, inp):
        await self.doSaveInput(inp)

    async def doGo(self, inp):
        if not await self.checkInput(inp):
            await self.promptForCorrection()
            return self
        await self.saveInput(inp)
        return await self.switch()

    async def doPromptForData(self):
        return await bot.bot.send_message(
                self.context.from_id, 
                self.data_prompt,
                parse_mode=ParseMode.HTML) 

    async def doPromptForCorrection(self):
        return await bot.bot.send_message(
                self.context.user_id,
                self.correction_prompt, 
                parse_mode=ParseMode.HTML) 

    async def doCheckInput(self, inp):
        return False

    async def doSaveInput(self, inp):
        pass

