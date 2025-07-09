from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_SamplerSettings_DualScheduler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}


    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = ("pipe", any, any, any, "INT", "FLOAT", "FLOAT", "UPSCALE_MODEL", "FLOAT")
    RETURN_NAMES = ("pipe", "sampler", "scheduler", "scheduler_2", "steps", "cfg", "flux_guidance", "upscale_model", "scale_by")

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, pipe=None, ):
        sampler, scheduler, scheduler_2, steps, cfg, flux_guidance, upscale_model, scale_by  = pipe
        
        return pipe, sampler, scheduler, scheduler_2, steps, cfg, flux_guidance, upscale_model, scale_by

NODE_NAME = 'Pipe Out Sampler Settings (Dual-Scheduler) [RvTools]'
NODE_DESC = 'Pipe Out Sampler Settings (Dual-Scheduler)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings_DualScheduler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
