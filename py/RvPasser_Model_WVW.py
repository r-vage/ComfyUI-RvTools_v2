from ..core import CATEGORY

class RvPasser_WAN_Model:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"model": ("WANVIDEOMODEL",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("WANVIDEOMODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "passthrough"

    def passthrough(self, model):
        return model,

NODE_NAME = 'Pass WAN_Model [RvTools]'
NODE_DESC = 'Pass WAN_Model'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_WAN_Model
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
