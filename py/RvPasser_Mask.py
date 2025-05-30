from ..core import CATEGORY

class RvPasser_Masks:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"mask": ("MASK",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("MASK",)
    FUNCTION = "passthrough"

    def passthrough(self, mask):
        return mask,

NODE_NAME = 'Pass Mask [RvTools]'
NODE_DESC = 'Pass Mask'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Masks
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
