from ..core import CATEGORY

class RvSwitch_ImageEmbeds_MultiSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Purge_VRAM": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "input1": ("WANVIDIMAGE_EMBEDS", {"forceInput": True}),
                "input2": ("WANVIDIMAGE_EMBEDS", {"forceInput": True}),
                "input3": ("WANVIDIMAGE_EMBEDS", {"forceInput": True}),
                "input4": ("WANVIDIMAGE_EMBEDS", {"forceInput": True}),
                "input5": ("WANVIDIMAGE_EMBEDS", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHESWW.value
    RETURN_TYPES = ("WANVIDIMAGE_EMBEDS",)
    RETURN_NAMES = ("image_embeds",)

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
            raise ValueError("Missing Input: Multi Image_Embeds Switch has no active Input")

NODE_NAME = 'WAN Image_Embeds Multi-Switch [RvTools]'
NODE_DESC = 'WAN Image_Embeds Multi-Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_ImageEmbeds_MultiSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
