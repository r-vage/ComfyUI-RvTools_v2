import os
import folder_paths

from datetime import datetime
from ..core import CATEGORY
from .anytype import AnyType

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

class RvFolders_ProjectFolder_Video:
    resolution =     ["Custom",
                      "480x832",
                      "576x1024",
                      "--- 9:16 ---",
                      "240x426 (240p)",              
                      "360x640 (360p)",
                      "480x853 (SD)",
                      "720x1280 (HD)",
                      "1080x1920 (FullHD)",
                      "1440x2560 (2K)",
                      "2160x3840 (4K)",
                      "4320x7680 (8K)",
                      "--- 16:9 ---",
                      "832x480",
                      "1024x576",
                      "426x240 (240p)",              
                      "640x360 (360p)",
                      "853x480 (SD)",
                      "1280x720x (HD)",
                      "1920x1080 (FullHD)",
                      "2560x1440 (2K)",
                      "3840x2160 (4K)",
                      "7680x4320 (8K)",                      
                      ]

    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "project_root_name": ("STRING", {"multiline": False, "default": "vGEN"}),
                "date_time_format": ("STRING", {"multiline": False, "default": "%Y-%m-%d"}),
                "add_date_time": (["disable", "prefix", "postfix"], {"default": "postfix"}),
                "batch_folder_name": ("STRING", {"multiline": False, "default": "batch_{}"}),                
                "create_batch_folder": ("BOOLEAN", {"default": False}),
                "relative_path": ("BOOLEAN", {"default": True}),
                "resolution": (cls.resolution,),
                "width": ("INT", {"default": 576, "min": 16, "max": MAX_RESOLUTION, "step": 1},),
                "height": ("INT", {"default": 1024, "min": 16, "max": MAX_RESOLUTION, "step": 1},),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
                "frame_rate": ("FLOAT", {"default": 30.0, "min": 8, "max": 240}),
                "frame_load_cap": ("INT", {"default": 81, "min": 1, "max": MAX_RESOLUTION, "step": 4},),
                "skip_first_frames": ("INT", {"default": 0, "min": 0, "max": 4096}),
                "select_every_nth": ("INT", {"default": 1, "min": 1, "max": 100}),
                

            },
            "optional": {
                "batch_no": (any, {"forceInput": True})
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("STRING", "INT",   "INT",    "INT",        "FLOAT",      "INT",            "INT",               "INT")
    RETURN_NAMES = ("path",   "width", "height", "batch_size", "frame_rate", "frame_load_cap", "skip_first_frames", "select_every_nth")
    
    FUNCTION = "execute"
    
    def execute(self, project_root_name, add_date_time, date_time_format, relative_path, create_batch_folder, batch_folder_name, batch_size, frame_rate, frame_load_cap, skip_first_frames, select_every_nth, resolution, width, height, batch_no=None):

        mDate = format_datetime(date_time_format)
        new_path = project_root_name

        if add_date_time == "prefix":
            new_path = os.path.join(mDate, project_root_name)
        elif add_date_time == "postfix":
            new_path = os.path.join(project_root_name, mDate)

        if create_batch_folder:
           folder_name_parsed = format_variables(batch_folder_name, batch_no)
           new_path = os.path.join(new_path, folder_name_parsed)

        if(resolution == "480x832"):
            width, height = 480, 832
        if(resolution == "576x1024"):
            width, height = 576, 1024 
        if(resolution == "240x426 (240p)"):
            width, height = 240, 426
        if(resolution == "360x640 (360p)"):
            width, height = 360, 640
        if(resolution == "480x853 (SD)"):
            width, height = 480, 853
        if(resolution == "720x1280 (HD)"):
            width, height = 720, 1280
        if(resolution == "1080x1920 (FullHD)"):
            width, height = 1080, 1920
        if(resolution == "1440x2560 (2K)"):
            width, height = 1440, 2560
        if(resolution == "2160x3840 (4K)"):
            width, height = 2160, 3840
        if(resolution == "4320x7680 (8K)"):
            width, height = 4320, 7680

        if(resolution == "832x480"):
            width, height = 832, 480
        if(resolution == "1024x576"):
            width, height = 1024, 576
        if(resolution == "426x240 (240p)"):
            width, height = 426, 240
        if(resolution == "640x360 (360p)"):
            width, height = 640, 360
        if(resolution == "853x480 (SD)"):
            width, height = 853, 480
        if(resolution == "1280x720x (HD)"):
            width, height = 1280, 720
        if(resolution == "1920x1080 (FullHD)"):
            width, height = 1920, 1080
        if(resolution == "2560x1440 (2K)"):
            width, height = 2560, 1440
        if(resolution == "3840x2160 (4K)"):
            width, height = 3840, 2160
        if(resolution == "7680x4320 (8K)"):
            width, height = 7680, 4320


        if relative_path:
            return ("./" + new_path, width, height, batch_size, frame_rate, frame_load_cap, skip_first_frames, select_every_nth)
        else:
            return (os.path.join(self.output_dir, new_path), width, height, batch_size, frame_rate, frame_load_cap, skip_first_frames, select_every_nth)
    

NODE_NAME = 'Project Folder Video [RvTools]'
NODE_DESC = 'Project Folder Video'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvFolders_ProjectFolder_Video
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
