import bot              

import services.sessionManager as sessionManager
from services.loopManager import loopManager

sm = sessionManager.get()


def main():
    import middleware
    middleware.setup(bot.dp)

    import filters
    filters.setup(bot.dp)

    import handlers

    loopManager.getLoop().create_task( sm.dangling_sessions_control_loop() )
    bot.executor.start_polling(bot.dp, skip_updates=True)

if __name__ == '__main__':
    main()

