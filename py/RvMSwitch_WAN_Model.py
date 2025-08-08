from ..core import CATEGORY

class RvMSwitch_WAN_Model:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Purge_VRAM": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "input1": ("WANVIDEOMODEL", {"forceInput": True}),
                "input2": ("WANVIDEOMODEL", {"forceInput": True}),
                "input3": ("WANVIDEOMODEL", {"forceInput": True}),
                "input4": ("WANVIDEOMODEL", {"forceInput": True}),
                "input5": ("WANVIDEOMODEL", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHESWW.value
    RETURN_TYPES = ("WANVIDEOMODEL",)
    RETURN_NAMES = ("model",)

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
            raise ValueError("Missing Input: Multi Switch WAN_Model has no active Input")

NODE_NAME = 'WAN_Model Multi-Switch [RvTools]'
NODE_DESC = 'WAN_Model Multi-Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvMSwitch_WAN_Model
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
