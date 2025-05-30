from ..core import CATEGORY

class RvPasser_Integer:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"int1": ("INT", {"forceInput": True}),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("INT",)
    FUNCTION = "passthrough"

    def passthrough(self, int1):
        return int1,

NODE_NAME = 'Pass Integer [RvTools]'
NODE_DESC = 'Pass Integer'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Integer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
