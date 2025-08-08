from ..core import CATEGORY

class RvSwitch_TextEmbeds_MultiSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Purge_VRAM": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "input1": ("WANVIDEOTEXTEMBEDS", {"forceInput": True}),
                "input2": ("WANVIDEOTEXTEMBEDS", {"forceInput": True}),
                "input3": ("WANVIDEOTEXTEMBEDS", {"forceInput": True}),
                "input4": ("WANVIDEOTEXTEMBEDS", {"forceInput": True}),
                "input5": ("WANVIDEOTEXTEMBEDS", {"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.MULTISWITCHESWW.value
    RETURN_TYPES = ("WANVIDEOTEXTEMBEDS",)
    RETURN_NAMES = ("text_embeds",)

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
            raise ValueError("Missing Input: Multi Text_Embeds Switch has no active Input")

NODE_NAME = 'WAN Text_Embeds Multi-Switch [RvTools]'
NODE_DESC = 'WAN Text_Embeds Multi-Switch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSwitch_TextEmbeds_MultiSwitch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
