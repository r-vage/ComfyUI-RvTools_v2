import comfy

from ..core import CATEGORY

SAMPLERS_COMFY = comfy.samplers.KSampler.SAMPLERS

class RvPasser_Sampler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"sampler_name": (SAMPLERS_COMFY, {"forceInput": True}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value

    RETURN_TYPES = (SAMPLERS_COMFY,)
    RETURN_NAMES = ("sampler_name",)

    FUNCTION = "passthrough"

    def passthrough(self, sampler_name):
        return (sampler_name,)

NODE_NAME = 'Pass Sampler [RvTools]'
NODE_DESC = 'Pass Sampler'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Sampler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
