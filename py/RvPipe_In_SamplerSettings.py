from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_SamplerSettings:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
                },
                "optional":{
                    "sampler": (any,),
                    "scheduler": (any,),
                    "steps": ("INT",{"forceInput": True,}),
                    "cfg": ("FLOAT",{"forceInput": True,}),
                    "flux_guidance": ("FLOAT",{"forceInput": True,}),
                    "denoise": ("FLOAT",{"forceInput": True,}),
                    "sigmas_denoise": ("FLOAT",{"forceInput": True,}),
                    "noise_strength": ("FLOAT",{"forceInput": True,}),
                    "seed": ("INT",{"forceInput": True,}),
                }}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",)
    RETURN_NAMES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, sampler = None, scheduler = None, steps = None, cfg = None, flux_guidance = None, denoise = None, sigmas_denoise = None, noise_strength = None, seed = None):
        pipe = sampler, scheduler, steps, cfg, flux_guidance, denoise, sigmas_denoise, noise_strength, seed
        
        return (pipe,)

NODE_NAME = 'Pipe In Sampler Settings NIS [RvTools]'
NODE_DESC = 'Pipe In Sampler Settings NIS'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_SamplerSettings
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
