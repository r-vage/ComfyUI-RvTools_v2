from ..core import CATEGORY, AnyType

any = AnyType("*")

class RvConversion_ComboToString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "combo": (any, {"default": []}),
                "separator": ("STRING", {"default": "$"}),
        }
    }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"

    def execute(self, combo, separator):
        if isinstance(combo, (str, float, int, bool)):
            return (combo,)
        return (separator.join(combo),)

NODE_NAME = 'Combo to String [RvTools]'
NODE_DESC = 'Combo to String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_ComboToString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}