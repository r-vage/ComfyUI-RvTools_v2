from ..core import CATEGORY, AnyType
import re

any = AnyType("*")

class RvPipe_Out_FilenameGenerator:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = ("pipe", "INT",              "INT",               "INT",               "BOOLEAN",       "STRING", "STRING",)
    RETURN_NAMES = ("pipe", "frame_load_cap",   "mask_last_frames",  "mask_first_frames", "simple_combine", "files",  "files_join",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, pipe=None, ):
        
        frame_load_cap, mask_last_frames, mask_first_frames, simple_combine, file_dict, join_dict = pipe

        files = ""
        files_join = ""

        if not file_dict in (None, '', 'undefined', 'none') :
            files = str(file_dict.get("FILE"))
            files = re.sub("^\[", "", files)
            files = re.sub("\]", "", files)
            files = re.sub("\'", "", files)

            #print(f"File: {files} ")

        if not join_dict in (None, '', 'undefined', 'none') :
            files_join = str(join_dict.get("JOIN"))
            files_join = re.sub("^\[", "", files_join)
            files_join = re.sub("\]", "", files_join)
            files_join = re.sub("\'", "", files_join)

            #print(f"File: {files_join} ")

        return pipe, frame_load_cap, mask_last_frames, mask_first_frames, simple_combine, files, files_join

NODE_NAME = 'Pipe Out VC-Filename Generator [RvTools]'
NODE_DESC = 'Pipe Out VC-Filename Generator'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_FilenameGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
