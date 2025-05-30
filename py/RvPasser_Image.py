from ..core import CATEGORY

class RvPasser_Image:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "passthrough"

    def passthrough(self, image):
        return image,

NODE_NAME = 'Pass Images [RvTools]'
NODE_DESC = 'Pass Images'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Image
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
