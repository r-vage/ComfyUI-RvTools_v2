from ..core import CATEGORY

class RvPasser_PipeLine:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"pipe": ("PIPE_LINE",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("PIPE_LINE",)
    FUNCTION = "passthrough"

    def passthrough(self, pipe):
        return pipe,

NODE_NAME = 'Pass Pipeline (CR) [RvTools]'
NODE_DESC = 'Pass Pipeline (CR)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_PipeLine
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
