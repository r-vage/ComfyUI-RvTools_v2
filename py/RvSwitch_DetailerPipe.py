from ..core import CATEGORY

class RvSwitch_DetailerPipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("DETAILER_PIPE", {"forceInput": True}),
                "input2": ("DETAILER_PIPE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("DETAILER_PIPE",)  
    RETURN_NAMES = ("DETAILER_PIPE",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Detailer Pipe Switch [RvTools]'
NODE_DESC = 'Detailer Pipe Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_DetailerPipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
