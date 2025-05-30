#from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_Generation_Data:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe", "INT", "FLOAT", "STRING", "STRING", "STRING", "STRING", "STRING", "INT", "INT", "INT", "STRING", "STRING",)
    RETURN_NAMES = ("pipe", "steps", "cfg", "sampler_name", "scheduler", "positive", "negative", "modelname", "width", "height", "seed_value", "loras", "vae_name",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        steps, cfg, sampler_name, scheduler, positive, negative, modelname, width, height, seed_value, loras, vae_name = pipe
        return pipe, steps, cfg, sampler_name, scheduler, positive, negative, modelname, width, height, seed_value, loras, vae_name

NODE_NAME = 'Pipe Out Generation Data [RvTools]'
NODE_DESC = 'Pipe Out Generation Data'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_Generation_Data
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
