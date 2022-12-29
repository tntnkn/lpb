from bot import bot
import services.sessionManager as sessionManager

from aiogram.types import ParseMode

sm = sessionManager.get()

async def send_unsolicited_message(from_id, text):
    resp = await bot.send_message(from_id, text, parse_mode=ParseMode.HTML)
    sm.memoMessage(from_id, resp)
    return resp

