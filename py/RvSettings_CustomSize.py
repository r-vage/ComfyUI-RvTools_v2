from ..core import CATEGORY

MAX_RESOLUTION = 32768

class RvSettings_CustomSize:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 16, "max": MAX_RESOLUTION, "step": 8},),
                "height": ("INT", {"default": 512, "min": 16, "max": MAX_RESOLUTION, "step": 8},),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("width","height",)

    FUNCTION = "execute"

    def execute(self, width, height,):
        return (width,height,)

NODE_NAME = 'Custom Size [RvTools]'
NODE_DESC = 'Custom Size'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_CustomSize
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
