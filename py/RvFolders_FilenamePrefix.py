import os

from ..core import CATEGORY, AnyType, format_datetime, format_date_time, format_variables

any = AnyType("*")

class RvFolders_FilenamePrefix:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"forceInput": True}),
                "file_name_prefix": ("STRING", {"multiline": False, "default": "image"}),
                "add_date_time": (["disable", "prefix", "postfix"],),
                "date_time_format": ("STRING", {"multiline": False, "default": "%Y-%m-%d_%H:%M:%S"}),
            },
            "optional": {
                "input_variables": (any,)
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "execute"

    def execute(self, path, file_name_prefix, add_date_time, date_time_format, input_variables=None):
        filename_name_parsed = format_variables(file_name_prefix, input_variables)
        if add_date_time == "disable":
            new_path = os.path.join(path, filename_name_parsed)
        else:
            new_path = os.path.join(path, format_date_time(filename_name_parsed, add_date_time, date_time_format))
        return (new_path,)

NODE_NAME = 'Add Filename Prefix [RvTools]'
NODE_DESC = 'Add Filename Prefix'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvFolders_FilenamePrefix
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
