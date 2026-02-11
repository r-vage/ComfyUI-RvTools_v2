import comfy  # type: ignore
import comfy.sd  # type: ignore
import folder_paths  # type: ignore

from ..core import CATEGORY

class RvSettings_Sampler_Settings_Flux_SGS:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Steps": ("INT", {"default": 20, "min": 1, "step": 1}),
                "CFG": ("FLOAT", {"default": 3.50, "min": 0.00, "step": 0.01}),
                "Flux_Guidance": ("FLOAT", {"default": 3.50, "min": 0.00, "step": 0.01}),
                "Denoise": ("FLOAT", {"default": 1.0, "min": 0.00, "max": 1.0, "step": 0.10}),
                "Noise_Seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True,}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, Steps, CFG, Flux_Guidance, Denoise, Noise_Seed):

        rlist = []
        rlist.append(int(Steps))
        rlist.append(float(CFG))
        rlist.append(float(Flux_Guidance))
        rlist.append(float(Denoise))
        rlist.append(int(Noise_Seed))

        return (rlist,)

NODE_NAME = 'Sampler Settings SGS (Flux) [RvTools]'
NODE_DESC = 'Sampler Settings SGS (Flux)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Sampler_Settings_Flux_SGS
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
