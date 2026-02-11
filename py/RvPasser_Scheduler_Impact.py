import comfy  # type: ignore

from ..core import CATEGORY

SCHEDULERS_IMPACT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]']

class RvPasser_Scheduler_Impact:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"scheduler": (SCHEDULERS_IMPACT, {"forceInput": True}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (SCHEDULERS_IMPACT,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "passthrough"
    DEPRECATED = True

    def passthrough(self, scheduler):
        return (scheduler,)    

NODE_NAME = 'Pass Scheduler (Impact) [RvTools]'
NODE_DESC = 'Pass Scheduler (Impact)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Scheduler_Impact
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
