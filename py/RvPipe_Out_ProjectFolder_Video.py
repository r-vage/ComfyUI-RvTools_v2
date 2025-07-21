from ..core import CATEGORY

class RvPipe_Out_ProjectFolder_Video:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("pipe", "INT",   "INT",    "INT",        "FLOAT",      "INT",            "INT",               "INT", "STRING",)
    RETURN_NAMES = ("pipe",   "width", "height", "batch_size", "frame_rate", "frame_load_cap", "skip_first_frames", "select_every_nth", "path",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        width, height, batch_size, frame_rate, frame_load_cap, skip_first_frames, select_every_nth, path = pipe
                
        return pipe, width, height, batch_size, frame_rate, frame_load_cap, skip_first_frames, select_every_nth, path

NODE_NAME = 'Pipe Out Project Folder Video [RvTools]'
NODE_DESC = 'Pipe Out Project Folder Video'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_ProjectFolder_Video
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
