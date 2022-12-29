from . import stateInterface
from utils.messaging import send_unsolicited_message
import bot

class justSendMessage(stateInterface):
    def __init__(self, context, prev=None):
        super().__init__(context, prev)
        self.next       = None
        self.message_id = None
        self.message    = None

    async def go(self, *args, **kwargs):
        self = await super().go(*args, **kwargs)
        if self.message_id is None:
            resp = await send_unsolicited_message(
                    self.context.from_id, self.message)
            self.message_id = resp.from_id
        return await self.go_next()

    async def handleExistingMessage(self):
        if self.message_id:
            await bot.bot.delete_message(
                chat_id     = self.context.from_id,
                message_id  = self.message_id)
            self.message_id = None

    async def go_next(self):
        await self.finish()
        try:
            return await self.next.go()
        except:
            self.next = self.next(self.context, self.prev)
        return await self.next.go()

