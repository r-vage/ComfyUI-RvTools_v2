import os
import folder_paths  # type: ignore

from datetime import datetime
from ..core import CATEGORY, AnyType, RESOLUTION_PRESETS, RESOLUTION_MAP

any = AnyType("*")

MAX_RESOLUTION = 32768

def format_datetime(datetime_format):
    today = datetime.now()
    try:
        timestamp = today.strftime(datetime_format)
    except:
        timestamp = today.strftime("%Y-%m-%d-%H%M%S")

    return timestamp

def format_date_time(string, position, datetime_format):
    today = datetime.now()
    if position == "prefix":
        return f"{today.strftime(datetime_format)}_{string}"
    if position == "postfix":
        return f"{string}_{today.strftime(datetime_format)}"

def format_variables(string, input_variables):
    if input_variables:
        variables = str(input_variables).split(",")
        return string.format(*variables)
    else:
        return string

class RvFolders_ProjectFolder_v2:

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "project_root_name": ("STRING", {"multiline": False, "default": "MyProject"}),
                "date_time_format": ("STRING", {"multiline": False, "default": "%Y-%m-%d"}),
                "add_date_time": (["disable", "prefix", "postfix"], {"default": "postfix"}),
                "batch_folder_name": ("STRING", {"multiline": False, "default": "batch_{}"}),                
                "create_batch_folder": ("BOOLEAN", {"default": False}),
                "relative_path": ("BOOLEAN", {"default": True}),
                "resolution": (RESOLUTION_PRESETS,),
                "width": ("INT", {"default": 512, "min": 16, "max": MAX_RESOLUTION, "step": 8},),
                "height": ("INT", {"default": 512, "min": 16, "max": MAX_RESOLUTION, "step": 8},),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
            },
            "optional": {
                "batch_no": (any, {"forceInput": True})
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("STRING", "INT",   "INT",    "INT")
    RETURN_NAMES = ("path",   "width", "height", "batch_size")
    
    FUNCTION = "execute"
    
    def execute(self, project_root_name, add_date_time, date_time_format, relative_path, create_batch_folder, batch_folder_name, batch_size, resolution, width, height, batch_no=None):

        mDate = format_datetime(date_time_format)
        new_path = project_root_name

        if add_date_time == "prefix":
            new_path = os.path.join(mDate, project_root_name)
        elif add_date_time == "postfix":
            new_path = os.path.join(project_root_name, mDate)

        if create_batch_folder:
           folder_name_parsed = format_variables(batch_folder_name, batch_no)
           new_path = os.path.join(new_path, folder_name_parsed)

        # Map resolution preset to width/height using centralized dictionary
        if resolution in RESOLUTION_MAP:
            width, height = RESOLUTION_MAP[resolution]


        if relative_path:
            return ("./" + new_path, width, height, batch_size)
        else:
            return (os.path.join(self.output_dir, new_path), width, height, batch_size)
    

NODE_NAME = 'Project Folder v2 [RvTools]'
NODE_DESC = 'Project Folder v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvFolders_ProjectFolder_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
