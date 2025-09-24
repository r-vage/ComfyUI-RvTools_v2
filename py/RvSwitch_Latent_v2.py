from ..core import CATEGORY

class RvSwitch_Latent_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),
                "Purge_VRAM": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "input1": ("LATENT", {"forceInput": True}),
                "input2": ("LATENT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SWITCHES.value
    RETURN_TYPES = ("LATENT",)  
    RETURN_NAMES = ("latent",)
    
    FUNCTION = "execute"

    def execute(self, Input, Purge_VRAM, input1=None, input2=None,):
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

        if Input == 1:
            return (input1,)
        else:
            return (input2,)

NODE_NAME = 'Latent Switch v2 [RvTools]'
NODE_DESC = 'Latent Switch v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Latent_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
