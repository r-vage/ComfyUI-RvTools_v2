import comfy

from ..core import CATEGORY

SCHEDULERS_EFFICIENT = comfy.samplers.KSampler.SCHEDULERS + ['AYS SD1', 'AYS SDXL', 'AYS SVD']

class RvSelector_Scheduler_Efficient:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"scheduler_efficient": (SCHEDULERS_EFFICIENT,),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_EFFICIENT,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "execute"

    def execute(self, scheduler_efficient):
        return (scheduler_efficient,)    

NODE_NAME = 'Scheduler Selector (Efficient) [RvTools]'
NODE_DESC = 'Scheduler Selector (Efficient)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_Scheduler_Efficient
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
