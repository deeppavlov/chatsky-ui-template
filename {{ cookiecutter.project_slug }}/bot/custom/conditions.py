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


class HelloCnd(BaseCondition):

    async def call(self, ctx: Context) -> bool:
        return await cnd.ExactMatch('hello')(ctx)

class YesCnd(BaseCondition):

    async def call(self, ctx: Context) -> bool:
        return await cnd.ExactMatch('yes')(ctx)

class NoCnd(BaseCondition):

    async def call(self, ctx: Context) -> bool:
        return await cnd.ExactMatch('no')(ctx)
