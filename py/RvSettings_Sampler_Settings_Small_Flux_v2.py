import comfy  # type: ignore
import comfy.sd  # type: ignore
import folder_paths  # type: ignore

from ..core import CATEGORY

SAMPLERS_COMFY = comfy.samplers.KSampler.SAMPLERS
SCHEDULERS_ANY = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]', 'OSS FLUX', 'OSS Wan', 'simple_test']

class RvSettings_Sampler_Settings_Small_Flux_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Sampler": (SAMPLERS_COMFY,),
                "Scheduler": (SCHEDULERS_ANY,),
                "Steps": ("INT", {"default": 20, "min": 1, "step": 1}),
                "CFG": ("FLOAT", {"default": 3.50, "min": 0.00, "step": 0.01}),
                "Flux_Guidance": ("FLOAT", {"default": 3.50, "min": 0.00, "step": 0.01}),
                "Denoise": ("FLOAT", {"default": 1.0, "min": 0.00, "max": 1.0, "step": 0.10}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, Sampler, Scheduler, Steps, CFG, Flux_Guidance, Denoise):

        rlist = []
        rlist.append(Sampler)
        rlist.append(Scheduler)
        rlist.append(int(Steps))
        rlist.append(float(CFG))
        rlist.append(float(Flux_Guidance))
        rlist.append(float(Denoise))

        return (rlist,)

NODE_NAME = 'Sampler Settings Small v2 (Flux) [RvTools]'
NODE_DESC = 'Sampler Settings Small v2 (Flux)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Sampler_Settings_Small_Flux_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
