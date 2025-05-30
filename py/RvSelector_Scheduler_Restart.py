
from ..core import CATEGORY

SCHEDULERS_RESTART = ('normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform', 'beta', 'simple_test')

class RvSelector_Scheduler_Restart:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"scheduler_restart": (SCHEDULERS_RESTART,),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SELECTOR.value
    RETURN_TYPES = (SCHEDULERS_RESTART,)
    RETURN_NAMES = ("scheduler",)

    FUNCTION = "execute"

    def execute(self, scheduler_restart):
        return (scheduler_restart,)

    @classmethod
    def VALIDATE_INPUTS(self, scheduler_restart):
        return True

NODE_NAME = 'Scheduler Selector (Restart) [RvTools]'
NODE_DESC = 'Scheduler Selector (Restart)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_Scheduler_Restart
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
