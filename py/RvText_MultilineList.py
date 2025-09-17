from ..core import CATEGORY

class RvText_Multiline:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("string", "string_list")

    OUTPUT_IS_LIST = (False, True)

    FUNCTION = "execute"

    def execute(self, string=""):
        string_list = string.strip()
        string_list_out = string_list.split('\n')

        return (string, string_list_out,)

NODE_NAME = 'String Multiline with List [RvTools]'
NODE_DESC = 'String Multiline with List'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvText_Multiline
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
