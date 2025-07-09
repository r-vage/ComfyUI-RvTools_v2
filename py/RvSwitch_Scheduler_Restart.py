from .anytype import *
from ..core import CATEGORY

SCHEDULERS_RESTART = ('normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'beta', 'simple_test')

class RvSwitch_Scheduler_Restart:
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
    RETURN_TYPES = (SCHEDULERS_RESTART,) 
    RETURN_NAMES = ("scheduler",)
    
    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Scheduler Switch (Restart) [RvTools]'
NODE_DESC = 'Scheduler Switch (Restart)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Scheduler_Restart
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
