from ..core import CATEGORY

class RvSwitch_Mask:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("MASK", {"forceInput": True}),
                "input2": ("MASK", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("MASK",)  
    RETURN_NAMES = ("mask",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Mask Switch [RvTools]'
NODE_DESC = 'Mask Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Mask
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
