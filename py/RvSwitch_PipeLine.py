from ..core import CATEGORY

class RvSwitch_PipeLine:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": ("PIPE_LINE", {"forceInput": True}),
                "input2": ("PIPE_LINE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("PIPE_LINE",)  
    RETURN_NAMES = ("PIPE_LINE",)
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Pipe-Line Switch [RvTools]'
NODE_DESC = 'Pipe-Line Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_PipeLine
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
