from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_SamplerSettings_Small_Flux:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",  any,       any,        "INT",   "FLOAT", "FLOAT")
    RETURN_NAMES = ("pipe", "sampler", "scheduler", "steps", "cfg",   "flux_guidance")

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        sampler, scheduler, steps, cfg, flux_guidance  = pipe
        
        return pipe, sampler, scheduler, steps, cfg, flux_guidance

NODE_NAME = 'Pipe Out Sampler Settings Small (Flux) [RvTools]'
NODE_DESC = 'Pipe Out Sampler Settings Small (Flux)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings_Small_Flux
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
