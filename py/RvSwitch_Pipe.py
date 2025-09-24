from ..core import CATEGORY

class RvSwitch_Pipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "pipe1": ("pipe",),
                "pipe2": ("pipe",),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("pipe",) 
    
    FUNCTION = "execute"

    def execute(self, Input, pipe1=None, pipe2=None,):

        if Input == 1:
            return (pipe1,)
        else:
            return (pipe2,)

NODE_NAME = 'Pipe Switch [RvTools]'
NODE_DESC = 'Pipe Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Pipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
