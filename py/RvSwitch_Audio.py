from ..core import CATEGORY

class RvSwitch_Audio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "audio1": ("AUDIO", {"forceInput": True}),
                "audio2": ("AUDIO", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("AUDIO",)   
    
    FUNCTION = "execute"

    def execute(self, Input, audio1=None, audio2=None,):

        if Input == 1:
            return (audio1,)
        else:
            return (audio2,)

NODE_NAME = 'Audio Switch [RvTools]'
NODE_DESC = 'Audio Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Audio
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
