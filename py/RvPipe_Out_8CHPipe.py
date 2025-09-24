from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

class RvPipe_Out_8CHPipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = ("pipe", any, any, any, any, any, any, any, any,)
    RETURN_NAMES = ("pipe", "any_1", "any_2", "any_3", "any_4", "any_5", "any_6", "any_7", "any_8",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, pipe=None,):
        any_1, any_2, any_3, any_4, any_5, any_6, any_7, any_8 = pipe
        return pipe, any_1, any_2, any_3, any_4, any_5, any_6, any_7, any_8

NODE_NAME = 'Pipe Out 8CH [RvTools]'
NODE_DESC = 'Pipe Out 8CH'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_8CHPipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
