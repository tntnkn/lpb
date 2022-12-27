from filters.user   import isPromtingForUserInfo, isFillingUserInfoForm, isSelectingUserConditionsOptions
from states.general import gettingUserInfoFormInput, noParticularActionState
from static.types   import userSession
import services.sessionManager as sessionManager
import bot
from static.guides  import guide_court, guide_quorum, guide_fee, guide_comission

sm = sessionManager.get()


# --- Commands Handlers

@bot.dp.message_handler(commands=['guide_court'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_court)

@bot.dp.message_handler(commands=['guide_quorum'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_quorum)

@bot.dp.message_handler(commands=['guide_comission'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_comission)

@bot.dp.message_handler(commands=['guide_fee'])
async def startCommandHandler(message: bot.types.Message):
    resp = await message.reply(guide_fee)

@bot.dp.message_handler(commands=['start'])
async def startCommandHandler(message: bot.types.Message):
    from_id = message.from_id
    session = sm.getSession(from_id)
    if session.current_state:
        session = await sm.resetSession(from_id)
    resp = await message.reply("Давайте сделаем иск!")
    session.current_state = gettingUserInfoFormInput(session)
    session.current_state = await session.current_state.go()
    sm.memoMessage(from_id, message)
    sm.memoMessage(from_id, resp)

from states.general import gettingUserInfo 
@bot.dp.message_handler(commands=['start'])
async def startCommandHandler(message: bot.types.Message):
    from_id = message.from_id
    session = sm.getSession(from_id)
    if session.current_state:
        session = await sm.resetSession(from_id)
    resp = await message.reply("Давайте сделаем иск!")
    session.current_state = gettingUserInfoFormInput(session)
    session.current_state = await session.current_state.go()
    sm.memoMessage(from_id, message)
    sm.memoMessage(from_id, resp)

@bot.dp.message_handler(commands=['help']) 
async def testHandler(message: bot.types.Message):
    await messageFallbackHandler(message=message)


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
