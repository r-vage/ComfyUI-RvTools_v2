import comfy

from ..core import CATEGORY

SCHEDULERS_EFFICIENT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SD1', 'AYS SDXL', 'AYS SVD']

class RvSelector_Scheduler_ComfyUI_Efficient:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler_comfy": (comfy.samplers.KSampler.SCHEDULERS,),
                "scheduler_efficient": (SCHEDULERS_EFFICIENT,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (
        comfy.samplers.KSampler.SCHEDULERS,
        SCHEDULERS_EFFICIENT,)
    RETURN_NAMES = ("comfy", "efficient",)

    FUNCTION = "execute"

    def execute(self, scheduler_comfy, scheduler_efficient):
        return (scheduler_comfy, scheduler_efficient,)

NODE_NAME = 'Scheduler Selector (ComfyUI+Efficient) [RvTools]'
NODE_DESC = 'Scheduler Selector (ComfyUI+Efficient)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_Scheduler_ComfyUI_Efficient
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
