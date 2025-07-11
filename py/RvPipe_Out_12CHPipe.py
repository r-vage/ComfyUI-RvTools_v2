from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

class RvPipe_Out_12CHPipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe", any, any, any, any, any, any, any, any, any, any, any, any,)
    RETURN_NAMES = ("pipe", "any_1", "any_2", "any_3", "any_4", "any_5", "any_6", "any_7", "any_8", "any_9", "any_10", "any_11", "any_12",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        any_1, any_2, any_3, any_4, any_5, any_6, any_7, any_8, any_9, any_10, any_11, any_12 = pipe
        return pipe, any_1, any_2, any_3, any_4, any_5, any_6, any_7, any_8, any_9, any_10, any_11, any_12

NODE_NAME = 'Pipe Out 12CH [RvTools]'
NODE_DESC = 'Pipe Out 12CH'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_12CHPipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
