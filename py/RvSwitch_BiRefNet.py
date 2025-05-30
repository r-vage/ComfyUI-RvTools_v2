from ..core import CATEGORY

class RvSwitch_BiRefNet:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("BIREFNET_MODEL", {"forceInput": True}),
                "input2": ("BIREFNET_MODEL", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("BIREFNET_MODEL",)  
    RETURN_NAMES = ("birefnet_model",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'BiRefNet Model Switch [RvTools]'
NODE_DESC = 'BiRefNet Model Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_BiRefNet
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
