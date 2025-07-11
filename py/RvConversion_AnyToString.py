from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

class RvConversion_AnyToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"input": (any, {"default": "", "forceInput": True}),
                }        
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ('STRING',)

    FUNCTION = 'execute'

    def execute(self, input):
        return (f'{input}',)

NODE_NAME = 'Any to String [RvTools]'
NODE_DESC = 'Any to String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_AnyToString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}