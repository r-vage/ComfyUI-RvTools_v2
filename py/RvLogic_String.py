from ..core import CATEGORY

class RvLogic_String:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"string": ("STRING", {"default": ""}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "execute"

    def execute(self, string=""):
        return (string,)

NODE_NAME = 'String [RvTools]'
NODE_DESC = 'String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvLogic_String
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
