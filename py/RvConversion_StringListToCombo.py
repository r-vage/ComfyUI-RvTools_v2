from ..core import CATEGORY, AnyType

any = AnyType("*")

class RvConversion_StringListToCombo:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"forceInput": True}),
                "separator": ("STRING", {"default": "$"}),
            },
            "optional": {
                "index": ("INT", {"default": 0}),
        }
    }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = (any,)
    FUNCTION = "execute"

    def execute(self, string, separator, index = 0):
        if isinstance(string, (float, int, bool)):
            return (string,)
        if separator == "" or separator == None or separator not in string:
            return (string,)
        # check length
        splitted = string.split(separator)
        if index >= len(splitted):
            return (splitted[-1],)
        return (splitted[index],)

NODE_NAME = 'Stringlist to Combo [RvTools]'
NODE_DESC = 'Stringlist to Combo'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_StringListToCombo
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
