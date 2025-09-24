from ..core import CATEGORY

class RvSwitch_Latent:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("LATENT", {"forceInput": True}),
                "input2": ("LATENT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("LATENT",)  
    RETURN_NAMES = ("latent",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Latent Switch [RvTools]'
NODE_DESC = 'Latent Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Latent
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
