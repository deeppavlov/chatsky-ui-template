from dff.script import Context
from dff import Pipeline

def is_upper_case(ctx: Context, pipeline: Pipeline):
    return ctx.last_request.text.isupper()
