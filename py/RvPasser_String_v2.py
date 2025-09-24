from ..core import CATEGORY

class RvPasser_String_v2:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"string": ("STRING", {"forceInput": True, "default": ""}),
                             "Purge_VRAM": ("BOOLEAN", {"default": False}),
                             }}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("STRING",)
    FUNCTION = "passthrough"

    def passthrough(self, Purge_VRAM, string):
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

        return string,

NODE_NAME = 'Pass String v2 [RvTools]'
NODE_DESC = 'Pass String v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_String_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
