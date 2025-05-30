import comfy

from .anytype import *
from ..core import CATEGORY

SCHEDULERS_COMFY = comfy.samplers.KSampler.SCHEDULERS

class RvSwitch_Scheduler:
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

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_COMFY,) 
    RETURN_NAMES = ("scheduler",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Scheduler Switch [RvTools]'
NODE_DESC = 'Scheduler Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Scheduler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
