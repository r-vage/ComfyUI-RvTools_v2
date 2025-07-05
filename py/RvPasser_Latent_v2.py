from ..core import CATEGORY

class RvPasser_Latent_v2:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "latent": ("LATENT",),
                              "Purge_VRAM": ("BOOLEAN", {"default": False}),
                             }}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "passthrough"

    def passthrough(self, Purge_VRAM, latent):
        if Purge_VRAM == True:
            try:
                import torch
                import torch.cuda
                import gc
                import comfy.model_management
 
                gc.collect()
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                    torch.cuda.ipc_collect()

                comfy.model_management.unload_all_models()
                comfy.model_management.soft_empty_cache()
            except:
                pass


        return latent,

NODE_NAME = 'Pass Latent v2 [RvTools]'
NODE_DESC = 'Pass Latent v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Latent_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
