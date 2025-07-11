import comfy
import comfy.sd
import folder_paths

from spandrel import ModelLoader, ImageModelDescriptor

from ..core import CATEGORY

UPSCALE_MODELS = folder_paths.get_filename_list("upscale_models") + ["None"]

SAMPLERS_COMFY = comfy.samplers.KSampler.SAMPLERS
SCHEDULERS_ANY = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]', 'OSS FLUX', 'OSS Wan', 'simple_test']

class RvSettings_Sampler_DualScheduler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Sampler": (SAMPLERS_COMFY,),
                "Scheduler": (SCHEDULERS_ANY,),
                "Scheduler_2": (SCHEDULERS_ANY,),
                "Steps": ("INT", {"default": 20, "min": 1, "step": 1}),
                "CFG": ("FLOAT", {"default": 3.5, "min": 0.00, "step": 0.01}),
                "Flux_Guidance": ("FLOAT", {"default": 3.50, "min": 0.0, "step": 0.01}),
            },
            "optional": {
                "Upscale_Model": (UPSCALE_MODELS, {"default": "None"}),
                "Scale_By": ("FLOAT", {"default": 0.50, "min": 0.00, "step": 0.10}),
            },

        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, Sampler, Scheduler, Scheduler_2, Steps, CFG, Flux_Guidance, Upscale_Model=None, Scale_By=None):
        UpscaleModel = None
        
        if Upscale_Model not in (None, 'undefined', 'None'):
            model_path = folder_paths.get_full_path("upscale_models", Upscale_Model)
            sd = comfy.utils.load_torch_file(model_path, safe_load=True)
            if "module.layers.0.residual_group.blocks.0.norm1.weight" in sd:
                sd = comfy.utils.state_dict_prefix_replace(sd, {"module.":""})
            UpscaleModel = ModelLoader().load_from_state_dict(sd).eval()

            if not isinstance(UpscaleModel, ImageModelDescriptor):
                UpscaleModel=None
                raise Exception("Upscale model must be a single-image model.")
       

        rlist = []
        rlist.append(Sampler)
        rlist.append(Scheduler)
        rlist.append(Scheduler_2)
        rlist.append(int(Steps))
        rlist.append(float(CFG))
        rlist.append(float(Flux_Guidance))
        rlist.append(UpscaleModel)
        rlist.append(float(Scale_By))

        return (rlist,)

NODE_NAME = 'Sampler Settings (Dual-Scheduler) [RvTools]'
NODE_DESC = 'Sampler Settings (Dual-Scheduler)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Sampler_DualScheduler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
