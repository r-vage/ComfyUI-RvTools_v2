from ..core import CATEGORY

class RvPasser_VAE:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"vae": ("VAE",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value

    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("vae",)

    FUNCTION = "passthrough"

    def passthrough(self, vae):
        return (vae,)

NODE_NAME = 'Pass Vae [RvTools]'
NODE_DESC = 'Pass Vae'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_VAE
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
