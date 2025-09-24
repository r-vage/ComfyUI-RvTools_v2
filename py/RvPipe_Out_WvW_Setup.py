from ..core import CATEGORY

class RvPipe_Out_WvW_Setup:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    
    RETURN_TYPES = ("pipe", "INT",   "FLOAT", "FLOAT",       "INT",         "INT",)
    RETURN_NAMES = ("pipe", "steps", "cfg",   "model_shift", "steps_start", "steps_end",)

    FUNCTION = "execute"

    #pipe: steps, cfg, model_shift, steps_start, steps_end
    def execute(self, pipe=None, ):
        steps, cfg, model_shift, steps_start, steps_end  = pipe
        
        return pipe, steps, cfg, model_shift, steps_start, steps_end

NODE_NAME = 'Pipe Out WanVideo Setup [RvTools]'
NODE_DESC = 'Pipe Out WanVideo Setup'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_WvW_Setup
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
