from ..core import CATEGORY

class RvPasser_Model:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"model": ("MODEL",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("MODEL",)
    FUNCTION = "passthrough"

    def passthrough(self, model):
        return model,

NODE_NAME = 'Pass Model [RvTools]'
NODE_DESC = 'Pass Model'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Model
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
