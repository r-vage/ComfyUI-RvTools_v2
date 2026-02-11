from ..core import CATEGORY, RESOLUTION_PRESETS

class RvSettings_Resolution_All:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"resolution": (RESOLUTION_PRESETS,),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.IMAGE.value
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("width", "height")

    FUNCTION = "execute"

    def execute(self, resolution):
        from ..core import RESOLUTION_MAP
        width, height = RESOLUTION_MAP.get(resolution, (512, 512))
        return (int(width), int(height))

NODE_NAME = 'Aspect Ratio (All) [RvTools]'
NODE_DESC = 'Aspect Ratio (All)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Resolution_All
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
