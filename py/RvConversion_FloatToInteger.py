from ..core import CATEGORY

class RvConversion_FloatToInteger:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"_float": ("FLOAT", {"default": 0.0, "forceInput": True}),
                }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("INT",)

    FUNCTION = "execute"

    def execute(self, _float):
        return (int(_float),)

NODE_NAME = 'Float to Integer [RvTools]'
NODE_DESC = 'Float to Integer'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_FloatToInteger
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}