from ..core import CATEGORY

class RvPasser_Audio:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"audio": ("AUDIO",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("AUDIO",)
    FUNCTION = "passthrough"

    def passthrough(self, audio):
        return audio,
    
NODE_NAME = 'Pass Audio [RvTools]'
NODE_DESC = 'Pass Audio'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Audio
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
