import os
import folder_paths  # type: ignore
import json

from datetime import datetime
from ..core import CATEGORY, AnyType, VIDEO_RESOLUTION_PRESETS, VIDEO_RESOLUTION_MAP

any = AnyType("*")

MAX_RESOLUTION = 32768

batchnum = int(0)
skipnum = int(0)

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

class RvFolders_ProjectFolder_Video_Pipe_v2:

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
                "create_batch_folder": ("BOOLEAN", {"default": True}),
                "relative_path": ("BOOLEAN", {"default": True}),
                "resolution": (VIDEO_RESOLUTION_PRESETS,),
                "width": ("INT", {"default": 576, "min": 16, "max": MAX_RESOLUTION, "step": 1},),
                "height": ("INT", {"default": 1024, "min": 16, "max": MAX_RESOLUTION, "step": 1},),
                "frame_rate": ("FLOAT", {"default": 30.0, "min": 8, "max": 240}),
                "frame_load_cap": ("INT", {"default": 81, "min": 1, "max": MAX_RESOLUTION, "step": 4},),
                "skip_first_frames": ("INT", {"default": 0, "min": 0, "max": 4096}),
                "skip_first_frames_calc": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "control_after_generate": True,}), 
                "select_every_nth": ("INT", {"default": 1, "min": 1, "max": 100}),
                "batch_number": ("INT", {"default": 1, "min": 1, "max": 0xffffffffffffffff, "control_after_generate": True,}),                

                

            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("pipe",)
        
    FUNCTION = "execute"
    
    def execute(self, project_root_name, add_date_time, date_time_format, relative_path, create_batch_folder, batch_folder_name, frame_rate, frame_load_cap, skip_first_frames, select_every_nth, resolution, width, height, batch_number, skip_first_frames_calc):

        mDate = format_datetime(date_time_format)
        new_path = project_root_name
        batchnum = batch_number
        skipnum = skip_first_frames_calc

        if add_date_time == "prefix":
            new_path = os.path.join(mDate, project_root_name)
        elif add_date_time == "postfix":
            new_path = os.path.join(project_root_name, mDate)

        if create_batch_folder:
           folder_name_parsed = format_variables(batch_folder_name, batchnum)
           new_path = os.path.join(new_path, folder_name_parsed)

        if skipnum > 0:
            try:
               skip_first_frames =  (skip_first_frames + (frame_load_cap * skipnum))
            except Exception as e:
                skip_first_frames =  0
                pass

        # Map resolution preset to width/height using centralized dictionary
        if resolution in VIDEO_RESOLUTION_MAP:
            width, height = VIDEO_RESOLUTION_MAP[resolution]

         #path, width, height, batch_size, frame_rate, frame_load_cap, skip_first_frames, select_every_nth
        Path = ""
        if relative_path:
            Path = "./" + new_path
        else:
            Path = os.path.join(self.output_dir, new_path)

        rlist = []
        rlist.append(int(width))
        rlist.append(int(height))
        rlist.append(int(1)) #batch size (not used)
        rlist.append(float(frame_rate))
        rlist.append(int(frame_load_cap))
        rlist.append(int(skip_first_frames))
        rlist.append(int(select_every_nth))
        rlist.append(str(Path))        

        return (rlist,)
       

NODE_NAME = 'Project Folder Video v2 (Pipe) [RvTools]'
NODE_DESC = 'Project Folder Video v2 (Pipe)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvFolders_ProjectFolder_Video_Pipe_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
