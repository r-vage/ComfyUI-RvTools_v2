from .anytype import *

from ..core import CATEGORY

class RvPipe_In_8CHPipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "pipe": ("pipe",),
                "any_1": (any,),
                "any_2": (any,),
                "any_3": (any,),
                "any_4": (any,),
                "any_5": (any,),
                "any_6": (any,),
                "any_7": (any,),
                "any_8": (any,),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, pipe=None, any_1=None, any_2=None, any_3=None, any_4=None, any_5=None, any_6=None, any_7=None, any_8=None):
        any_1_original = None
        any_2_original = None
        any_3_original = None
        any_4_original = None
        any_5_original = None
        any_6_original = None
        any_7_original = None
        any_8_original = None

        if pipe != None:
            any_1_original, any_2_original, any_3_original, any_4_original, any_5_original, any_6_original, any_7_original, any_8_original = pipe

        RBusAnyMod = []

        RBusAnyMod.append(any_1 if any_1 is not None else any_1_original)
        RBusAnyMod.append(any_2 if any_2 is not None else any_2_original)
        RBusAnyMod.append(any_3 if any_3 is not None else any_3_original)
        RBusAnyMod.append(any_4 if any_4 is not None else any_4_original)
        RBusAnyMod.append(any_5 if any_5 is not None else any_5_original)
        RBusAnyMod.append(any_6 if any_6 is not None else any_6_original)
        RBusAnyMod.append(any_7 if any_7 is not None else any_7_original)
        RBusAnyMod.append(any_8 if any_8 is not None else any_8_original)

        return (RBusAnyMod,)

NODE_NAME = 'Pipe In 8CH [RvTools]'
NODE_DESC = 'Pipe In 8CH'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_In_8CHPipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
