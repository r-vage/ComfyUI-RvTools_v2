from ..core import CATEGORY

class RvSwitch_Latent_MultiSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "input1": ("LATENT", {"forceInput": True}),
                "input2": ("LATENT", {"forceInput": True}),
                "input3": ("LATENT", {"forceInput": True}),
                "input4": ("LATENT", {"forceInput": True}),
                "input5": ("LATENT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHES.value
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)

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
            raise ValueError("Missing Input: Multi Latent Switch has no active Input")

NODE_NAME = 'Latent Multi-Switch [RvTools]'
NODE_DESC = 'Latent Multi-Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Latent_MultiSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
