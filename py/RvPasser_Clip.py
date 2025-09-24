from ..core import CATEGORY

class RvPasser_Clip:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"clip": ("CLIP",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "passthrough"

    def passthrough(self, clip):
        return clip,

NODE_NAME = 'Pass Clip [RvTools]'
NODE_DESC = 'Pass Clip'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Clip
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
