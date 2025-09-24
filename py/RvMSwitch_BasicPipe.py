from ..core import CATEGORY

class RvSwitch_BasicPipe_MultiSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "input1": ("BASIC_PIPE", {"forceInput": True}),
                "input2": ("BASIC_PIPE", {"forceInput": True}),
                "input3": ("BASIC_PIPE", {"forceInput": True}),
                "input4": ("BASIC_PIPE", {"forceInput": True}),
                "input5": ("BASIC_PIPE", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHES.value
    RETURN_TYPES = ("BASIC_PIPE",)

    FUNCTION = "execute"

    def execute(self, input1=None, input2=None, input3=None, input4=None, input5=None):
        

        if input1 != None:
            return (input1,)
        elif input2 != None:
            return (input2,)
        elif input3 != None:
            return (input3,)
        elif input4 != None:
            return (input4,)
        elif input5 != None:
            return (input5,)
        else:
            raise ValueError("Missing Input: Multi Pipe Switch has no active Input")

NODE_NAME = 'Basic Pipe Multi-Switch [RvTools]'
NODE_DESC = 'Basic Pipe Multi-Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_BasicPipe_MultiSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
