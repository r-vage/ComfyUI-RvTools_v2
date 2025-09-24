from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

class RvPipe_Out_SamplerSettings_Flux_Seed:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",  any,       any,        "INT",   "FLOAT", "FLOAT",         "FLOAT",   "INT")
    RETURN_NAMES = ("pipe", "sampler", "scheduler", "steps", "cfg",   "flux_guidance", "denoise", "seed")

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        sampler, scheduler, steps, cfg, flux_guidance, denoise, seed   = pipe
        
        return pipe, sampler, scheduler, steps, cfg, flux_guidance, denoise, seed

NODE_NAME = 'Pipe Out Sampler Settings (Flux+Seed) [RvTools]'
NODE_DESC = 'Pipe Out Sampler Settings (Flux+Seed)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings_Flux_Seed
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
