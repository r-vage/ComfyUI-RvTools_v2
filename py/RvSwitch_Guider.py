from ..core import CATEGORY

class RvSwitch_Guider:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("GUIDER", {"forceInput": True}),
                "input2": ("GUIDER", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("GUIDER",)  
    RETURN_NAMES = ("guider",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

    @classmethod
    def VALIDATE_INPUTS(self, Input):
        return True

NODE_NAME = 'Guider Switch [RvTools]'
NODE_DESC = 'Guider Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Guider
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
