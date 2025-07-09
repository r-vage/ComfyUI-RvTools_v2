
import comfy

from ..core import CATEGORY

SCHEDULERS_IMPACT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]']

class RvSelector_Scheduler_Impact:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"scheduler_impact": (SCHEDULERS_IMPACT,),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (SCHEDULERS_IMPACT,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, scheduler_impact):
        return (scheduler_impact,)    

NODE_NAME = 'Scheduler Selector (Impact) [RvTools]'
NODE_DESC = 'Scheduler Selector (Impact)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_Scheduler_Impact
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
