from ..core import CATEGORY

#i've created this to be used in managed groups
class RvPasser_Supir_Vae:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"SUPIR_VAE": ("SUPIRVAE",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("SUPIRVAE",)
    RETURN_NAMES = ("SUPIR_VAE",)
    FUNCTION = "passthrough"

    def passthrough(self, SUPIR_VAE):
        return SUPIR_VAE,

NODE_NAME = 'Pass SUPIR_VAE [RvTools]'
NODE_DESC = 'Pass SUPIR_VAE'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Supir_Vae
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}

