from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_SamplerSettings_Small_Flux_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",  any,       any,        "INT",   "FLOAT", "FLOAT", "FLOAT")
    RETURN_NAMES = ("pipe", "sampler", "scheduler", "steps", "cfg",   "flux_guidance", "denoise")

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        sampler, scheduler, steps, cfg, flux_guidance, denoise  = pipe
        
        return pipe, sampler, scheduler, steps, cfg, flux_guidance, denoise

NODE_NAME = 'Pipe Out Sampler Settings Small v2 (Flux) [RvTools]'
NODE_DESC = 'Pipe Out Sampler Settings Small v2 (Flux)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings_Small_Flux_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
