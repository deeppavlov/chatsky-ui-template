import re

from chatsky import Pipeline
from chatsky.script import Context, TRANSITIONS, RESPONSE, Message
import chatsky.script.conditions as cnd


def is_upper_case(ctx: Context, pipeline: Pipeline):
    return ctx.last_request.text.isupper()


