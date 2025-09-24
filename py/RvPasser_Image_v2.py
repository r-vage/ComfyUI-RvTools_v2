from ..core import CATEGORY

class RvPasser_Image_v2:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "image": ("IMAGE",),
                              "Purge_VRAM": ("BOOLEAN", {"default": False}),
                             }}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "passthrough"

    def passthrough(self, Purge_VRAM, image):
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


        return (image,)

NODE_NAME = 'Pass Images v2 [RvTools]'
NODE_DESC = 'Pass Images v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Image_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
