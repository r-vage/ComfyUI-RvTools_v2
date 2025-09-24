from ..core import CATEGORY

class RvSwitch_Image:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("IMAGE", {"forceInput": True}),
                "input2": ("IMAGE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("IMAGE",)  
    RETURN_NAMES = ("image",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Image Switch [RvTools]'
NODE_DESC = 'Image Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Image
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
