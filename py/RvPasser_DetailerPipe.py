from ..core import CATEGORY

class RvPasser_DetailerPipe:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"pipe": ("DETAILER_PIPE",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("DETAILER_PIPE",)
    FUNCTION = "passthrough"

    def passthrough(self, pipe):
        return pipe,

NODE_NAME = 'Pass Detailer Pipe [RvTools]'
NODE_DESC = 'Pass Detailer Pipe'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_DetailerPipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
