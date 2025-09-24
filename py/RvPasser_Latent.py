from ..core import CATEGORY

class RvPasser_Latent:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"latent": ("LATENT",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "passthrough"

    def passthrough(self, latent):
        return latent,

NODE_NAME = 'Pass Latent [RvTools]'
NODE_DESC = 'Pass Latent'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Latent
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
