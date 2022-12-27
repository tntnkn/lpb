class stateInterface():
    def __init__(self, context, prev=None):
        # it should at least know how the things ended up here.
        self.prev    = prev
        # it should also know about a context. 
        # context should have current_state property. 
        # current_state shoud be switched by the state when, well, switched.
        self.context = context

    async def go(self, *args, **kwargs):
        # perform steps of a machine while can. can switch state. 
        # it knows when to stop (usually when kind of user input is needed.
        # switches context's current_state to self.
        # the context should receive the last step or None, if done.
        self.context.current_state = self
        return self

    async def finish(self):
        # finish a particular step. don't go into the next one. do clean-up.
        # should return self.
        return self

    async def done(self):
        # like finish, but for all the machine.
        # should also indicate that all the machine is done.
        # should return None.
        if self.prev is None and self.next is None:
            return None
        tmp_prev = self.prev
        tmp_next = self.next
        self.prev = None
        self.next = None

        try:
            await tmp_prev.done()
        except:
            pass
        try:
            await tmp_next.done()
        except:
            pass

        self.prev = tmp_prev
        self.next = tmp_next
        await self.finish()

        return None

    async def reject(self):
        # invalidate this step (after invalidating all the subsequent ones).
        try:
            await self.next.reject()
        except:
            pass

    async def switch(self):
        # do clean-up.
        # switch to the next (or previous, or whatever) step.
        # do go() on success.
        return await self.finish().go()

    async def go_next(self):
        # switch to next and go()
        # if new next, then become it's new prev.
        if self.next is None:
            return await self.done()
        await self.finish()
        try:
            return await self.next.go()
        except:
            self.next = self.next(self.context, self)
        return await self.next.go()

    async def go_prev(self):
        # switch to prev and go()
        # the new prev know it's next itself!
        await self.finish()
        try:
            return await self.prev.go()
        except:
            self.prev = self.prev(self.context, None)
        return await self.prev.go()

