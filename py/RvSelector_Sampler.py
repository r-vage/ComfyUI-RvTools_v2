
import comfy

from ..core import CATEGORY

class RvSelector_Sampler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"sampler_name": (comfy.samplers.KSampler.SAMPLERS,),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value

    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS,)
    RETURN_NAMES = ("sampler_name",)

    FUNCTION = "execute"

    def execute(self, sampler_name):
        return (sampler_name,)

NODE_NAME = 'Sampler Selector [RvTools]'
NODE_DESC = 'Sampler Selector'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_Sampler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
