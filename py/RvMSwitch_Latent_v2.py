from ..core import CATEGORY

class RvSwitch_Latent_MultiSwitch_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Purge_VRAM": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "input1": ("LATENT", {"forceInput": True}),
                "input2": ("LATENT", {"forceInput": True}),
                "input3": ("LATENT", {"forceInput": True}),
                "input4": ("LATENT", {"forceInput": True}),
                "input5": ("LATENT", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHES.value
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)

    FUNCTION = "execute"

    def execute(self, Purge_VRAM, input1=None, input2=None, input3=None, input4=None, input5=None):
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
        

        if input1 != None:
            return (input1,)
        elif input2 != None:
            return (input2,)
        elif input3 != None:
            return (input3,)
        elif input4 != None:
            return (input4,)
        elif input5 != None:
            return (input5,)
        else:
            raise ValueError("Missing Input: Multi Latent Switch has no active Input")

NODE_NAME = 'Latent Multi-Switch v2 [RvTools]'
NODE_DESC = 'Latent Multi-Switch v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_Latent_MultiSwitch_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
