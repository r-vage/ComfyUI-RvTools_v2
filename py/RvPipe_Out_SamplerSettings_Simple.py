from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_SamplerSettings_Simple:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe", any, any, "INT", "FLOAT", "FLOAT", "UPSCALE_MODEL", "FLOAT")
    RETURN_NAMES = ("pipe", "sampler", "scheduler", "steps", "cfg", "flux_guidance", "upscale_model", "scale_by")

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        sampler, scheduler, steps, cfg, flux_guidance, upscale_model, scale_by  = pipe
        
        return pipe, sampler, scheduler, steps, cfg, flux_guidance, upscale_model, scale_by

NODE_NAME = 'Pipe Out Sampler Settings (Simple) [RvTools]'
NODE_DESC = 'Pipe Out Sampler Settings (Simple)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings_Simple
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
