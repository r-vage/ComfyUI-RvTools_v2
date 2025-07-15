from ..core import CATEGORY

class RvPipe_Out_Generation_Data_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe", "STRING",       "STRING",    "INT",   "FLOAT", "INT",        "INT",   "INT",     "STRING",   "STRING",   "STRING",     "STRING",   "STRING",)
    RETURN_NAMES = ("pipe", "sampler_name", "scheduler", "steps", "cfg",   "seed_value", "width", "height",  "positive", "negative", "modelname",  "vae_name", "loras",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        sampler_name, scheduler, steps, cfg, seed_value, width, height, positive, negative, modelname, vae_name, loras = pipe
        return pipe, sampler_name, scheduler, steps, cfg, seed_value, width, height, positive, negative, modelname, vae_name, loras

NODE_NAME = 'Pipe Out Generation Data II [RvTools]'
NODE_DESC = 'Pipe Out Generation Data II'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_Generation_Data_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
