from dff.script import Context
from dff import Pipeline
from dff.script import Context, TRANSITIONS, RESPONSE, Message
import dff.script.conditions as cnd

def is_upper_case(ctx: Context, pipeline: Pipeline):
    return ctx.last_request.text.isupper()
