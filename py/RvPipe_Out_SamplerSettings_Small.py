from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

class RvPipe_Out_SamplerSettings_Small:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",  any,       any,        "INT",   "FLOAT")
    RETURN_NAMES = ("pipe", "sampler", "scheduler", "steps", "cfg")

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        sampler, scheduler, steps, cfg  = pipe
        
        return pipe, sampler, scheduler, steps, cfg

NODE_NAME = 'Pipe Out Sampler Settings Small [RvTools]'
NODE_DESC = 'Pipe Out Sampler Settings Small'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings_Small
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
