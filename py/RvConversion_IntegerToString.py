from ..core import CATEGORY

class RvConversion_IntegerToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"int_": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "forceInput": True}),
                }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("STRING", )

    FUNCTION = 'execute'

    def execute(self, int_):
        return (f'{int_}',)

NODE_NAME = 'Integer to String [RvTools]'
NODE_DESC = 'Integer to String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_IntegerToString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
