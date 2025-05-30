import sys

from ..core import CATEGORY

class RvLogic_Float:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"_float": ("FLOAT", {"default": 1.00,"min": -sys.float_info.max,"max": sys.float_info.max,"step": 0.01}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("float",)

    FUNCTION = "execute"

    def execute(self, _float):
        return (_float,)

NODE_NAME = 'Float [RvTools]'
NODE_DESC = 'Float'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvLogic_Float
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
