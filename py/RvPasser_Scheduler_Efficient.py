import comfy

from ..core import CATEGORY

SCHEDULERS_EFFICIENT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SD1', 'AYS SDXL', 'AYS SVD']

class RvPasser_Scheduler_Efficient:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"scheduler": (SCHEDULERS_EFFICIENT, {"forceInput": True}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (SCHEDULERS_EFFICIENT,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "passthrough"
    DEPRECATED = True

    def passthrough(self, scheduler):
        return (scheduler,)    

NODE_NAME = 'Pass Scheduler (Efficient) [RvTools]'
NODE_DESC = 'Pass Scheduler (Efficient)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Scheduler_Efficient
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
