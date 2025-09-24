from ..core import CATEGORY

class RvPasser_Float:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"flt": ("FLOAT", {"forceInput": True}),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "passthrough"

    def passthrough(self, flt):
        return flt,

NODE_NAME = 'Pass Float [RvTools]'
NODE_DESC = 'Pass Float'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Float
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
