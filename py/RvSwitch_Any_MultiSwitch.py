from ..core import CATEGORY
from .anytype import *


class RvSwitch_Any_MultiSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "input1": (any, {}),
                "input2": (any, {}),
                "input3": (any, {}),
                "input4": (any, {}),
                "input5": (any, {}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHES.value
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("*",)

    FUNCTION = "execute"

    def execute(self, input1=None, input2=None, input3=None, input4=None, input5=None):
        

        if input1 != None:
            return (input1,)
        elif input2 != None:
            return (input2,)
        elif input3 != None:
            return (input3,)
        elif input4 != None:
            return (input4,)
        elif input5 != None:
            return (input5,)

        else:
            raise ValueError("Missing Input: Multi Any Switch has no active Input.")

NODE_NAME = 'Any Multi-Switch [RvTools]'
NODE_DESC = 'Any Multi-Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Any_MultiSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
