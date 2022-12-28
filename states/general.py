from aiogram.types import InputFile

from .base import stateInterface
import states.userInfo              as userInfo
import states.userInfoCheckup       as userInfoCheckup
import states.userCondition         as userCondition
import services.sessionManager      as sessionManager
import services.docgen              as docgen
from utils import send_unsolicited_message
import bot
import os

import logging

sm = sessionManager.get()

userInfoFirstState      = userInfo.askingName
checkingInfoFirstState  = userInfoCheckup.courtCheckup
userConditionFirstState = userCondition.startUserCondition


class noParticularActionState(stateInterface):
    # this one is needed for situations when user is sending an input
    # not attributive to any particular state
    def __init__(self, context=None, prev=None):
        super().__init__(context, prev)
        self.next = None

class globalState(stateInterface):
    # it assepts session as self.context.
    # being a context, session should at least have: 
    #       current_state, from_id, user_info and user_cond.
    # it also itself serves as a context for "sub-states".
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.from_id        = context.from_id
        self.current_state  = None
        self.default_state  = None
        self.next           = None

    async def go(self, smth=None, *args, **kwargs):
        self = await super().go()
        self.current_state = await self.current_state.go(smth, *args, **kwargs)
        if self.current_state is None:
            return await self.switch()
        return self

    async def finish(self):
        try:
            await self.current_state.done()
        except:
            logging.exception(self)
        self.current_state = self.default_state
        return self

    async def switch(self):
        return await self.go_next()


class gettingUserInfo(globalState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.user_info     = context.user_info
        self.default_state = userInfoFirstState(self)
        self.current_state = self.default_state
        self.next          = gettingUserInfoFormInput(context, self, False)

class gettingUserInfoFormInput(globalState):
    def __init__(self, context, prev=None, shall_enforce_input=True):
        super().__init__(context, prev)
        self.user_info     = context.user_info
        self.default_state = checkingInfoFirstState(self, None, None, 
                                                    shall_enforce_input)
        self.current_state = self.default_state
        self.next          = gettingUserCondition

class gettingUserCondition(globalState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.user_document = context.user_document
        self.user_condition= context.user_condition
        self.user_info     = context.user_info
        self.default_state = userConditionFirstState(self)
        self.current_state = self.default_state
        self.next          = creatingSuit

    async def go(self, smth=None, *args, **kwargs):
        try:
            self.current_state = await self.current_state.go(smth, *args)
        except:
            logging.exception("exception in gettingUserCondition.go()")
            await send_unsolicited_message(
                self.context.from_id,
                "Упс, видимо Вам сейчас надо нажать кнопку, а не написать!")
        if self.current_state is None:
            print("IS NONE!!!")
            print( vars(self.context.user_condition) )
            print( vars(self.context.user_document) )
            return await self.switch()
        return self

class creatingSuit(globalState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next    = sendingSuitToUser 

    async def go(self, smth=None, *args, **kwargs):
        self.context.current_state = self
        f_name = docgen.makeDocument(
                self.context.from_id, 
                self.context.user_info,
                self.context.user_condition,
                self.context.user_document)
        await self.finish()
        self.next = self.next(self.context, self)
        return await self.next.go(f_name, *args, **kwargs)
        
class sendingSuitToUser(globalState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next       = endingcontext

    async def go(self, f_name, *args, **kwargs):
        self.context.current_state = self
        f = InputFile(f_name, filename="Иск.docx")        
        await bot.bot.send_document(
                chat_id=self.context.from_id, document=f)
        os.remove(f_name)
        return await self.go_next()

class endingcontext(globalState):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next       = None

    async def go(self, smth=None, *args, **kwargs):
        self.context.current_state = self
        return await self.done()


defaultState = gettingUserInfo

