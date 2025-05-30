from ..core import CATEGORY

class RvPasser_Conditioning:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"conditioning": ("CONDITIONING",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "passthrough"

    def passthrough(self, conditioning):
        return conditioning,

NODE_NAME = 'Pass Conditioning [RvTools]'
NODE_DESC = 'Pass Conditioning'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Conditioning
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
