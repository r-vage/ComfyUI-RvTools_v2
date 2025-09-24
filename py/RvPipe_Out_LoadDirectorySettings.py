from ..core import CATEGORY

class RvPipe_Out_LoadDirectorySettings:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe", "STRING",    "INT",         "INT")
    RETURN_NAMES = ("pipe", "directory", "start_index", "load_cap")

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        directory, start_index, load_cap  = pipe
        
        return pipe, directory, start_index, load_cap

NODE_NAME = 'Pipe Out Load Directory Settings [RvTools]'
NODE_DESC = 'Pipe Out Load Directory Settings'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_LoadDirectorySettings
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
