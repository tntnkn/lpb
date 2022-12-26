
class loopManager():
    loop = None

    def getLoop():
        if loopManager.loop is None: 
            import asyncio
            loopManager.loop = asyncio.get_event_loop()
        return loopManager.loop

