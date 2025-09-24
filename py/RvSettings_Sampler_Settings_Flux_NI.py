import comfy
import comfy.sd
import folder_paths

from ..core import CATEGORY

SAMPLERS_COMFY = comfy.samplers.KSampler.SAMPLERS
SCHEDULERS_ANY = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]', 'OSS FLUX', 'OSS Wan', 'simple_test']

class RvSettings_Sampler_Settings_Flux_NI:
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
                "Sigmas_Denoise": ("FLOAT", {"default": 0.45, "min": 0.00, "step": 0.01}),
                "Noise_Strength": ("FLOAT", {"default": 0.50, "min": 0.00, "step": 0.01}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, Sampler, Scheduler, Steps, CFG, Flux_Guidance, Denoise, Sigmas_Denoise, Noise_Strength):

        rlist = []
        rlist.append(Sampler)
        rlist.append(Scheduler)
        rlist.append(int(Steps))
        rlist.append(float(CFG))
        rlist.append(float(Flux_Guidance))
        rlist.append(float(Denoise))
        rlist.append(float(Sigmas_Denoise))
        rlist.append(float(Noise_Strength))

        return (rlist,)

NODE_NAME = 'Sampler Settings (Flux) [RvTools]'
NODE_DESC = 'Sampler Settings (Flux)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Sampler_Settings_Flux_NI
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
