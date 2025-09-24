from ..core import CATEGORY

class RvSwitch_ControlNet:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("CONTROL_NET", {"forceInput": True}),
                "input2": ("CONTROL_NET", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("CONTROL_NET",)  
    RETURN_NAMES = ("cn",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'ControlNet Switch [RvTools]'
NODE_DESC = 'ControlNet Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_ControlNet
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
