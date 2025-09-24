from ..core import CATEGORY

class RvPasser_BasicPipe:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"pipe": ("BASIC_PIPE",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("BASIC_PIPE",)
    FUNCTION = "passthrough"

    def passthrough(self, pipe):
        return pipe,

NODE_NAME = 'Pass Basic Pipe [RvTools]'
NODE_DESC = 'Pass Basic Pipe'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_BasicPipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
