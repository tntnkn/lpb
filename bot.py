from aiogram import Bot, Dispatcher, executor, types
from services.loopManager import loopManager

#TODO: move into loadable config
API_TOKEN = 'TOKEN_HERE'

bot = Bot( token=API_TOKEN, loop=loopManager.getLoop() )
dp  = Dispatcher( bot, loop=loopManager.getLoop() )

