from ..core import CATEGORY, cstr
from .anytype import AnyType
import re, os

any = AnyType("*")

class RvPipe_Out_FilenameGenerator_v1:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value
    RETURN_TYPES = ("STRING", "STRING",    "INT",            "INT",               "INT",              "STRING",)
    RETURN_NAMES = ("path",   "rel_path",  "frame_load_cap", "mask_first_frames", "mask_last_frames", "files",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        
        path, frame_load_cap, mask_first_frames, mask_last_frames, file_dict = pipe

        files = ""

        rel_path = re.sub("(<?^.*output)", ".", path)
        #cstr(f"rel_path: {rel_path}").msg.print()
        
        if not file_dict in (None, '', 'undefined', 'none') :
            files = str(file_dict.get("FILE"))
            files = re.sub("^\[", "", files)
            files = re.sub("\]", "", files)
            files = re.sub("\'", "", files)

            #print(f"File: {files} ")


        return path, rel_path, frame_load_cap, mask_first_frames, mask_last_frames, files

NODE_NAME = 'Pipe Out VC-Filename Generator I [RvTools]'
NODE_DESC = 'Pipe Out VC-Filename Generator I'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_FilenameGenerator_v1
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
