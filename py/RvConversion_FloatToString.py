from ..core import CATEGORY

class RvConversion_FloatToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"float_": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1000000.0, "forceInput": True}),
                }        
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ('STRING',)

    FUNCTION = 'execute'

    def execute(self, float_):
        return (f'{float_}',)

NODE_NAME = 'Float to String [RvTools]'
NODE_DESC = 'Float to String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_FloatToString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}