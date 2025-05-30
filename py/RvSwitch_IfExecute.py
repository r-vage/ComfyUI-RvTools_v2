from ..core import CATEGORY
from .anytype import *

class RvSwitch_IfExecute:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "on_true": (any, {}),
                "on_false": (any, {}),
                "boolean": ("BOOLEAN", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = (any,)

    FUNCTION = "execute"

    def execute(self, on_true, on_false, boolean=True):

        if boolean:
            return (on_true,)
        else:
            return (on_false,)
 

NODE_NAME = 'IF A Else B [RvTools]'
NODE_DESC = 'IF A Else B'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_IfExecute
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
