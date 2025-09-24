
from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

SAMPLERS_RESTART = ['euler', 'euler_cfg_pp', 'euler_ancestral', 'euler_ancestral_cfg_pp', 'heun', 'heunpp2', 'dpm_2', 'dpm_2_ancestral', \
                    'lms', 'dpmpp_2s_ancestral', 'dpmpp_2m', 'dpmpp_2m_alt', 'ddpm', 'lcm', 'ipndm', 'ipndm_v', 'deis', 'ddim']


class RvSwitch_Sampler_Restart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {"default": [], "forceInput": True}),
                "input2": (any, {"default": [], "forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (SAMPLERS_RESTART,) 
    RETURN_NAMES = ("sampler_name",)
    
    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Sampler Switch (Restart) [RvTools]'
NODE_DESC = 'Sampler Switch (Restart)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Sampler_Restart
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
