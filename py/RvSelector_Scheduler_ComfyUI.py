
import comfy

from ..core import CATEGORY

class RvSelector_Scheduler_ComfyUI:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"scheduler_comfy": (comfy.samplers.KSampler.SCHEDULERS,),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (comfy.samplers.KSampler.SCHEDULERS,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, scheduler_comfy):
        return (scheduler_comfy,)

NODE_NAME = 'Scheduler Selector (ComfyUI) [RvTools]'
NODE_DESC = 'Scheduler Selector (ComfyUI)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_Scheduler_ComfyUI
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
