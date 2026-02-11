import comfy  # type: ignore

from ..core import CATEGORY, AnyType

any = AnyType("*")

class RvSwitch_Sampler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),            
            },
            "optional": {
                "input1": (any, {"default": [], "forceInput": True}),
                "input2": (any, {"default": [], "forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS,) 
    RETURN_NAMES = ("sampler_name",)
    
    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, Input, input1=None, input2=None,):

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Sampler Switch [RvTools]'
NODE_DESC = 'Sampler Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Sampler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
