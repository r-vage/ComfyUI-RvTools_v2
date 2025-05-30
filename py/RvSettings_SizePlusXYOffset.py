from ..core import CATEGORY

class RvSettings_SizePlusXYOffset:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Width": ("INT", {"default": 150}),
                "Height": ("INT", {"default": 20}),
            },
            "optional": {
                "Offset_Y": ("INT",{"default": 0}),
                "Offset_X": ("INT",{"default": 0}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("INT","INT","INT","INT",)
    RETURN_NAMES = ("width","height","offset_y","offset_x",)

    FUNCTION = "execute"

    def execute(self, Width, Height, Offset_Y, Offset_X):
        return (Width,Height,Offset_Y,Offset_X,)

NODE_NAME = 'Size + XY Offset [RvTools]'
NODE_DESC = 'Size + XY Offset'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_SizePlusXYOffset
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
