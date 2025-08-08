from ..core import CATEGORY

class RvSwitch_CacheArgs_MultiSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Purge_VRAM": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "input1": ("CACHEARGS", {"forceInput": True}),
                "input2": ("CACHEARGS", {"forceInput": True}),
                "input3": ("CACHEARGS", {"forceInput": True}),
                "input4": ("CACHEARGS", {"forceInput": True}),
                "input5": ("CACHEARGS", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHESWW.value
    RETURN_TYPES = ("CACHEARGS",)
    RETURN_NAMES = ("cache_args",)

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
            return (None,)

NODE_NAME = 'WAN Cache Args Multi-Switch [RvTools]'
NODE_DESC = 'WAN Cache Args Multi-Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_CacheArgs_MultiSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
