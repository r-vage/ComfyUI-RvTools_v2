import comfy

from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

SCHEDULERS_EFFICIENT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SD1', 'AYS SDXL', 'AYS SVD']

class RvSwitch_Scheduler_Efficient:
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
    RETURN_TYPES = (SCHEDULERS_EFFICIENT,) 
    RETURN_NAMES = ("scheduler",)
    
    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Scheduler Switch (Efficient) [RvTools]'
NODE_DESC = 'Scheduler Switch (Efficient)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Scheduler_Efficient
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
