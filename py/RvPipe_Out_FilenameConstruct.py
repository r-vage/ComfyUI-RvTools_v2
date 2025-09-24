from ..core import CATEGORY

class RvPipe_Out_FilenameConstruct:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = ("pipe", "INT",              "INT",               "INT",            "STRING",     "STRING",     "STRING",     "STRING",     "STRING",     "STRING",          "STRING",          "STRING",          "STRING",          "STRING",)
    RETURN_NAMES = ("pipe", "mask_frames_last", "mask_frames_first", "frame_load_cap", "filename_1", "filename_2", "filename_3", "filename_4", "filename_5", "filename_join_1", "filename_join_2", "filename_join_3", "filename_join_4", "filename_join_5",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, pipe=None, ):
        
        mask_frames_last, mask_frames_first, frame_load_cap, filename_1, filename_2, filename_3, filename_4, filename_5, filename_join_1, filename_join_2, filename_join_3, filename_join_4, filename_join_5 = pipe
        return pipe, mask_frames_last, mask_frames_first, frame_load_cap, filename_1, filename_2, filename_3, filename_4, filename_5, filename_join_1, filename_join_2, filename_join_3, filename_join_4, filename_join_5

NODE_NAME = 'Pipe Out Filename Construct [RvTools]'
NODE_DESC = 'Pipe Out Filename Construct'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_FilenameConstruct
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
