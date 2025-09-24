import sys

from ..core import CATEGORY

MAX_RESOLUTION = 32768

class RvLogic_WAN_Frames:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"value":  ("INT", {"default": 81,"min": 1,"max": MAX_RESOLUTION,"step": 4}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int",)

    FUNCTION = "execute"

    def execute(self, value):
        return (value,)

NODE_NAME = 'WAN_Frames [RvTools]'
NODE_DESC = 'WAN_Frames'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvLogic_WAN_Frames
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
