import asyncio
from time import time

import bot
from static.types import userSession, sessionInfo
from services.loopManager import loopManager


class sessionManager():
    instance = None

    def __init__(self):
        if sessionManager.instance is not None:
            return sessionManager.instance
        self.sessions = dict()
        self.DANGLING_SESSIONS_CHECKUP_STRIDE   = 20 * 60
        self.MAX_ALLOWED_DANGLING_TIME          = 60 * 60

    def get():
        if sessionManager.instance is None:
            sessionManager.instance = sessionManager()
        return sessionManager.instance

    def addSession(self, from_id):
        if not self.hasSession(from_id):
            self.sessions[from_id] = sessionInfo( userSession(from_id) )
        return self.sessions[from_id]

    def getSession(self, from_id, state=None):
        if not self.hasSession(from_id):
            return None
        return self.sessions[from_id].session

    def getSessionInfo(self, from_id):
        if not self.hasSession(from_id):
            return None
        return self.sessions[from_id]

    async def deleteSession(self, from_id):
        if not self.hasSession(from_id):
            return False
        session = self.getSession(from_id)
        if session.current_state:
            await session.current_state.done()
        await self.deleteLeftMessages(session)
        del self.sessions[from_id]
        return True

    async def deleteLeftMessages(self, session):
        for mess in session.left_messages:
            await bot.bot.delete_message(
                    chat_id=session.from_id,
                    message_id=mess.message_id)  

    async def resetSession(self, from_id):
        if not self.hasSession(from_id):
            return None
        session     = self.getSession(from_id)
        was_locked  = self.getSessionInfo(from_id).locked
        from_id     = session.from_id
        await self.deleteSession(from_id)
        sessionInfo = self.addSession(from_id)
        if was_locked:
            self.lockSession(from_id)
        return sessionInfo.session 

    def hasSession(self, from_id):
        return from_id in self.sessions

    def lockSession(self, from_id):
        if not self.hasSession(from_id):
            return False
        session_info = self.getSessionInfo(from_id)
        if session_info.locked:
            return False
        session_info.locked = True
        return True

    def unlockSession(self, from_id):
        if not self.hasSession(from_id):
            return False
        self.getSessionInfo(from_id).locked = False
        return True

    def recordSessionAction(self, from_id):
        if not self.hasSession(from_id):
            return False
        self.getSessionInfo(from_id).last_action_time = time()
        return True

    def memoMessage(self, from_id, mess):
        if not self.hasSession(from_id):
            return False
        self.getSession(from_id).left_messages.append(mess)
        return True
        
    async def dangling_sessions_control_loop(self):
        while True:
            await asyncio.sleep(self.DANGLING_SESSIONS_CHECKUP_STRIDE)
            await self.delete_dangling_sessions()

    async def delete_dangling_sessions(self):
        print("in delete_dangling_sessions()")
        now = time()
        print("now is: ", now)
        sessions_to_delete = list()
        for sessionInfo in self.sessions.values():
            print("last action is: ", sessionInfo.last_action_time)
            if now - sessionInfo.last_action_time > \
               self.MAX_ALLOWED_DANGLING_TIME:
                sessions_to_delete.append(sessionInfo.session.from_id)
                print("SESSION EXPIRED!")
        for from_id in sessions_to_delete:
            await self.deleteSession(from_id)
                    

def get():
    return sessionManager.get()

