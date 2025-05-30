import sys

from ..core import CATEGORY

class RvLogic_Integer:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"_int":  ("INT", {"default": 1,"min": -sys.maxsize,"max": sys.maxsize,"step": 1}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("int",)

    FUNCTION = "execute"

    def execute(self, _int):
        return (_int,)

NODE_NAME = 'Integer [RvTools]'
NODE_DESC = 'Integer'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvLogic_Integer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
