import re

from ..core import CATEGORY

class RvText_ReplaceString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "String": ("STRING", {"default": ""}),
                "Regex": ("STRING", {"default": ""}),
                "ReplaceWith": ("STRING", {"default": ""}),
            }
    }
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.TEXT.value
    RETURN_TYPES = ("STRING",)

    FUNCTION = "execute"
    
    def execute(self, String, Regex, ReplaceWith):
        # using regex
        return (re.sub(Regex, ReplaceWith, String),)

NODE_NAME = 'Replace String [RvTools]'
NODE_DESC = 'Replace String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvText_ReplaceString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
