from filters.user   import isPromtingForUserInfo, isFillingUserInfoForm, isSelectingUserConditionsOptions
from states.general import gettingUserInfoFormInput, noParticularActionState
from static.types   import userSession
import static.commands as c
import services.sessionManager as sessionManager
import bot
from static.guides  import guide_court, guide_how_to_sue, guide_quorum, guide_fee, guide_comission, guide_comissariat
from aiogram.types import ParseMode

sm = sessionManager.get()


# --- Commands Handlers

@bot.dp.message_handler(commands=['guides'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(c.mess.guides,parse_mode=ParseMode.HTML)

@bot.dp.message_handler(commands=['guide_court'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_court, parse_mode=ParseMode.HTML)

@bot.dp.message_handler(commands=['guide_how_to_sue'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_how_to_sue,parse_mode=ParseMode.HTML)

@bot.dp.message_handler(commands=['guide_quorum'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_quorum,parse_mode=ParseMode.HTML)

@bot.dp.message_handler(commands=['guide_comission'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_comission,parse_mode=ParseMode.HTML)

@bot.dp.message_handler(commands=['guide_comissariat'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_comissariat,parse_mode=ParseMode.HTML)

@bot.dp.message_handler(commands=['guide_fee'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_fee,parse_mode=ParseMode.HTML)

@bot.dp.message_handler(commands=['info'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(c.mess.info,parse_mode=ParseMode.HTML)

@bot.dp.message_handler(commands=['help'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(c.mess.help,parse_mode=ParseMode.HTML)

from states.general import gettingUserInfo 
@bot.dp.message_handler(commands=['start'])
async def startCommandHandler(message: bot.types.Message):
    from_id = message.from_id
    session = sm.getSession(from_id)
    if session.current_state:
        session = await sm.resetSession(from_id)
    resp = await message.reply("Давайте сделаем иск!\nОбратите внимание, что на обжалование решений призывной комиссии, таких как отказ в предоставлении АГС и призыв на военную службу, есть всего три месяца.\n\nЕсли у Вас возникнут трудоности, напишите нашим друзьям в @agsnowarbot, и Вам обязательно помогут.")
    session.current_state = gettingUserInfoFormInput(session)
    session.current_state = await session.current_state.go()
    sm.memoMessage(from_id, message)
    sm.memoMessage(from_id, resp)


# --- Test Commands Handlers

from states.general import gettingUserInfoFormInput 
@bot.dp.message_handler(commands=['form']) 
async def testHandler(message: bot.types.Message):
    from_id = message.from_id
    session = sm.getSession(from_id)
    if session.current_state:
        session = await sm.resetSession(from_id)
    session.current_state = gettingUserInfoFormInput(session)
    session.current_state = await session.current_state.go()
    sm.memoMessage(from_id, message)

from states.general import gettingUserCondition 
@bot.dp.message_handler(commands=['choise']) 
async def testHandler(message: bot.types.Message):
    from_id = message.from_id
    session = sm.getSession(from_id)
    if session.current_state:
        session = await sm.resetSession(from_id)
    session.current_state = gettingUserCondition(session)
    session.current_state = await session.current_state.go()
    sm.memoMessage(from_id, message)


# --- Text input handlers

@bot.dp.message_handler( isPromtingForUserInfo() )
@bot.dp.message_handler( isSelectingUserConditionsOptions() ) 
async def generalTextMessageHandler(message: bot.types.Message):
    session = sm.getSession(message.from_id)
    session.current_state = await session.current_state.go(message.text)
    sm.memoMessage(message.from_id, message)

@bot.dp.message_handler( isFillingUserInfoForm() ) 
async def generalFieldKeyboardInputHandler(message: bot.types.Message):
    session = sm.getSession(message.from_id)
    session.current_state = await session.current_state.go("changing", message.text)
    sm.memoMessage(message.from_id, message)


# --- Callback Query Handlers

@bot.dp.callback_query_handler( isFillingUserInfoForm() ) 
@bot.dp.callback_query_handler( isSelectingUserConditionsOptions() ) 
async def generalCallbackQueryHandler(callback: bot.types.CallbackQuery):
    session = sm.getSession(callback["from"]["id"])
    session.current_state = await session.current_state.go(session.cb_data)
    await callback.answer()


# --- Fallback Handlers

@bot.dp.message_handler() 
async def messageFallbackHandler(message: bot.types.Message):
    session = sm.getSession(message.from_id)
    if session.current_state is None: 
        session.current_state = noParticularActionState() 
    resp = await bot.bot.send_message(
           message.from_id, "Введите или нажмите /start, чтобы начать.")
    sm.memoMessage(message.from_id, message)
    sm.memoMessage(message.from_id, resp)

@bot.dp.callback_query_handler() 
async def callbackQueryFallbackHandler(callback: bot.types.CallbackQuery):
    session = sm.getSession(callback["from"]["id"].from_id)
    if session.current_state is None:
        session.current_state = noParticularActionState()
    resp = await bot.bot.send_message(
            callback["from"]["id"], "Введите или нажмите /start, чтобы начать.")
    sm.memoMessage(callback["from"]["id"], resp)
    await callback.answer()

