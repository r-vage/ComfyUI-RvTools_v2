
import comfy
from ..core import CATEGORY

SCHEDULERS_COMFY = comfy.samplers.KSampler.SCHEDULERS
SCHEDULERS_EFFICIENT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SD1', 'AYS SDXL', 'AYS SVD']
SCHEDULERS_IMPACT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SDXL', 'AYS SD1', 'AYS SVD', 'GITS[coeff=1.2]']
SCHEDULERS_RESTART = ('normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'beta', 'simple_test')

class RvSelector_Scheduler_All:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Comfy": (SCHEDULERS_COMFY,),
                "Efficient": (SCHEDULERS_EFFICIENT,),
                "Impact": (SCHEDULERS_IMPACT,),
                "Restart": (SCHEDULERS_RESTART,),
                }
            }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = (
        SCHEDULERS_COMFY,
        SCHEDULERS_EFFICIENT,
        SCHEDULERS_IMPACT,
        SCHEDULERS_RESTART,
        )
    RETURN_NAMES = ("comfy", "efficient", "impact", "restart",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, Comfy, Efficient, Impact, Restart):
        return (Comfy, Efficient, Impact, Restart,)

NODE_NAME = 'Scheduler Selector (All) [RvTools]'
NODE_DESC = 'Scheduler Selector (All)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_Scheduler_All
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
