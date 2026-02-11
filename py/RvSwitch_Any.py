from ..core import CATEGORY, AnyType

any = AnyType("*")

class RvSwitch_Any:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {}),
                "input2": (any, {}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = (any,)   
    
    FUNCTION = "execute"

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Any Switch [RvTools]'
NODE_DESC = 'Any Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Any
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
