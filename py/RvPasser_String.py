from ..core import CATEGORY

class RvPasser_String:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"string": ("STRING", {"forceInput": True, "default": ""}),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("STRING",)
    FUNCTION = "passthrough"

    def passthrough(self, string):
        return string,

NODE_NAME = 'Pass String [RvTools]'
NODE_DESC = 'Pass String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_String
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
