import re

from chatsky import (
    Context,
    TRANSITIONS,
    RESPONSE,
    Message,
    Pipeline,
    BaseCondition,
    Transition as Tr,
    conditions as cnd,
)


class hello_cnd(BaseCondition):

    async def call(self, ctx: Context) -> bool:
        return await cnd.ExactMatch('hello')(ctx)

class yes_cnd(BaseCondition):

    async def call(self, ctx: Context) -> bool:
        return await cnd.ExactMatch('yes')(ctx)

class no_cnd(BaseCondition):

    async def call(self, ctx: Context) -> bool:
        return await cnd.ExactMatch('no')(ctx)
