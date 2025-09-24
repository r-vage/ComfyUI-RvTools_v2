import comfy

from ..core import CATEGORY

SCHEDULERS_COMFY = comfy.samplers.KSampler.SCHEDULERS

class RvPasser_Scheduler_ComfyUI:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"scheduler": (SCHEDULERS_COMFY, {"forceInput": True}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (SCHEDULERS_COMFY,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "passthrough"
    DEPRECATED = True

    def passthrough(self, scheduler):
        return (scheduler,)    

NODE_NAME = 'Pass Scheduler (ComfyUI) [RvTools]'
NODE_DESC = 'Pass Scheduler (ComfyUI)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Scheduler_ComfyUI
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
