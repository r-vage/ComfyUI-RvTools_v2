
import comfy  # type: ignore
from ..core import CATEGORY

SCHEDULERS_EFFICIENT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SD1', 'AYS SDXL', 'AYS SVD']
SCHEDULERS_IMPACT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]', 'OSS FLUX', 'OSS Wan', 'simple_test']

class RvSelector_Scheduler_Efficient_Impact:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler_efficient": (SCHEDULERS_EFFICIENT,),
                "scheduler_impact": (SCHEDULERS_IMPACT,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (
        SCHEDULERS_EFFICIENT,
        SCHEDULERS_IMPACT,)
    RETURN_NAMES = ("efficient", "impact",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, scheduler_efficient, scheduler_impact):
        return (scheduler_efficient, scheduler_impact,)

NODE_NAME = 'Scheduler Selector (Efficient+Impact) [RvTools]'
NODE_DESC = 'Scheduler Selector (Efficient+Impact)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_Scheduler_Efficient_Impact
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
