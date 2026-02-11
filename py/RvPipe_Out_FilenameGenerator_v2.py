from ..core import CATEGORY, cstr
from ..core import AnyType
import re, os

any = AnyType("*")

class RvPipe_Out_FilenameGenerator_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value
    RETURN_TYPES = ("STRING", "STRING",    "INT",            "BOOLEAN",        "STRING", "STRING",)
    RETURN_NAMES = ("path",   "rel_path",  "frame_load_cap", "simple_combine", "files",  "files_join",)

    FUNCTION = "execute"

    def execute(self, pipe=None, ):
        
        path, frame_load_cap, simple_combine, file_dict, join_dict = pipe

        files = ""
        files_join = ""

        rel_path = re.sub("(<?^.*output)", ".", path)
        #cstr(f"relative path {rel_path}").msg.print()

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

        return path, rel_path, frame_load_cap, simple_combine, files, files_join

NODE_NAME = 'Pipe Out VC-Filename Generator II [RvTools]'
NODE_DESC = 'Pipe Out VC-Filename Generator II'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_FilenameGenerator_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
