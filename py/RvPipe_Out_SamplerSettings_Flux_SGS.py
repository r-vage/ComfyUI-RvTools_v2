from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_SamplerSettings_Flux_SGS:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe", "INT",   "FLOAT", "FLOAT",         "FLOAT",   "INT")
    RETURN_NAMES = ("pipe", "steps", "cfg",   "flux_guidance", "denoise", "seed")

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        steps, cfg, flux_guidance, denoise, seed   = pipe
        
        return pipe, steps, cfg, flux_guidance, denoise, seed

NODE_NAME = 'Pipe Out Sampler Settings SGS (Flux) [RvTools]'
NODE_DESC = 'Pipe Out Sampler Settings SGS (Flux)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings_Flux_SGS
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
