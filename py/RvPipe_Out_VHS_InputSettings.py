#from .anytype import *

from ..core import CATEGORY

class RvPipe_Out_VHS_InputSettings:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe", "INT", "INT", "INT", "INT", "INT", "INT", ["center","top", "bottom", "left", "right"], ["lanczos", "nearest", "bilinear", "bicubic", "area", "nearest-exact"], "FLOAT",)
    RETURN_NAMES = ("pipe", "load_cap", "skip_first_frames", "select_every_nth", "overlap", "images_in_preview", "images_in_filter_previews", "preview_crop_pos", "preview_crop_interpol", "frame_rate",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        load_cap, skip_first_frames, select_every_nth, overlap, images_in_preview, images_in_filter_previews, preview_crop_pos, preview_crop_interpol, frame_rate  = pipe
        
        return pipe, load_cap, skip_first_frames, select_every_nth, overlap, images_in_preview, images_in_filter_previews, preview_crop_pos, preview_crop_interpol, frame_rate

NODE_NAME = 'Pipe Out VHS Input Settings [RvTools]'
NODE_DESC = 'Pipe Out VHS Input Settings'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_VHS_InputSettings
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
