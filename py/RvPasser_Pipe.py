from ..core import CATEGORY

class RvPasser_Pipe:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"pipe": ("pipe",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("pipe",)
    FUNCTION = "passthrough"

    def passthrough(self, pipe):
        return pipe,

NODE_NAME = 'Pass Pipe [RvTools]'
NODE_DESC = 'Pass Pipe'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Pipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}

