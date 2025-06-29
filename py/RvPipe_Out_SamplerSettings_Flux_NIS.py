from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_SamplerSettings_Flux_NISeed:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",  any,       any,        "INT",   "FLOAT", "FLOAT", "FLOAT", "FLOAT", "FLOAT", "INT")
    RETURN_NAMES = ("pipe", "sampler", "scheduler", "steps", "cfg",   "flux_guidance", "denoise","sigmas_denoise","noise_strength", "seed")

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        sampler, scheduler, steps, cfg, flux_guidance, denoise, sigmas_denoise, noise_strength, seed   = pipe
        
        return pipe, sampler, scheduler, steps, cfg, flux_guidance, denoise, sigmas_denoise, noise_strength, seed

NODE_NAME = 'Pipe Out Sampler Settings NIS (Flux) [RvTools]'
NODE_DESC = 'Pipe Out Sampler Settings NIS (Flux)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings_Flux_NISeed
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
