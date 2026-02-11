import comfy  # type: ignore

from ..core import CATEGORY

SAMPLERS_COMFY = comfy.samplers.KSampler.SAMPLERS
SCHEDULERS_ANY = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]', 'OSS FLUX', 'OSS Wan', 'simple_test']

class RvSettings_Sampler_Selection:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Sampler": (SAMPLERS_COMFY,),
                "Scheduler": (SCHEDULERS_ANY,),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, Sampler, Scheduler):
        rlist = []
        rlist.append(Sampler)
        rlist.append(Scheduler)
        rlist.append(int(0))            #keep for compatibility with pipe sampler settings small
        rlist.append(float(0))          #keep for compatibility

        return (rlist,)

NODE_NAME = 'Sampler Selection [RvTools]'
NODE_DESC = 'Sampler Selection'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Sampler_Selection
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
