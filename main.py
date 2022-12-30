import asyncio

import bot              

import services.sessionManager as sessionManager
from services.loopManager import loopManager

import logging
logging.basicConfig(filename="log.txt", filemode="a")

import json
import static.commands as c

sm = sessionManager.get()


def main():
    import middleware
    middleware.setup(bot.dp)

    import filters
    filters.setup(bot.dp)

    import handlers
    
    loop = loopManager.getLoop()
    set_commands_task = loop.create_task(
        bot.bot.set_my_commands(commands=json.dumps([
            {'command' : c.start,       'description' : c.desc.start},
            {'command' : c.help,        'description' : c.desc.help},
            {'command' : c.info,        'description' : c.desc.info},
            {'command' : c.guides,      'description' : c.desc.guides},

        ]))
    )

    dangling_sessions_control_task = loop.create_task( 
        sm.dangling_sessions_control_loop() )

    bot.executor.start_polling(bot.dp, skip_updates=True)

if __name__ == '__main__':
    main()

