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

class RvFolders_ProjectFolder_Video_Pipe:
    resolution =     ["Custom",
                      "512x512 (1:1)",              
                      "512x682 (3:4)",
                      "512x768 (2:3)",
                      "512x910 (9:16)",
                      "512x952 (1:1.85)",
                      "512x1024 (1:2)",
                      "512x1224 (1:2.39)",
                      "640x1536 (9:21)",
                      "682x512 (4:3)",
                      "768x512 (3:2)",
                      "768x1344 (9:16)",
                      "832x1216 (2:3)",
                      "896x1152 (3:4)",
                      "910x512 (16:9)",
                      "952x512 (1.85:1)",
                      "1024x512 (2:1)",
                      "1024x1024 (1:1)",
                      "1152x896 (4:3)",
                      "1216x832 (3:2)",
                      "1224x512 (2.39:1)",
                      "1344x768 (16:9)",
                      "1536x640 (21:9)" 
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
                "width": ("INT", {"default": 576, "min": 16, "max": MAX_RESOLUTION, "step": 8},),
                "height": ("INT", {"default": 1024, "min": 16, "max": MAX_RESOLUTION, "step": 8},),
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
    RETURN_TYPES = ("pipe",)
        
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

        #if(resolution == "Custom"):
            #width, height = 512, 512
        if(resolution == "512x512 (1:1)"):
            width, height = 512, 512
        if(resolution == "512x682 (3:4)"):
            width, height = 512, 682
        if(resolution == "512x768 (2:3)"):
            width, height = 512, 768
        if(resolution == "512x910 (9:16)"):
            width, height = 512, 910
        if(resolution == "512x952 (1:1.85)"):
            width, height = 512, 952
        if(resolution == "512x1024 (1:2)"):
            width, height = 512, 1024
        if(resolution == "512x1224 (1:2.39)"):
            width, height = 512, 1224
        if(resolution == "682x512 (4:3)"):
            width, height = 682, 512
        if(resolution == "768x512 (3:2)"):
            width, height = 768, 512
        if(resolution == "910x512 (16:9)"):
            width, height = 910, 512
        if(resolution == "952x512 (1.85:1)"):
            width, height = 952, 512
        if(resolution == "1024x512 (2:1)"):
            width, height = 1024, 512
        if(resolution == "1224x512 (2.39:1)"):
            width, height = 1224, 512
        #sdxl
        if(resolution == "640x1536 (9:21)"):
            width, height = 640, 1536
        if(resolution == "768x1344 (9:16)"):
            width, height = 768, 1344
        if(resolution == "832x1216 (2:3)"):
            width, height = 832, 1216
        if(resolution == "896x1152 (3:4)"):
            width, height = 896, 1152
        if(resolution == "1024x1024 (1:1)"):
            width, height = 1024, 1024
        if(resolution == "1152x896 (4:3)"):
            width, height = 1152, 896
        if(resolution == "1216x832 (3:2)"):
            width, height = 1216, 832
        if(resolution == "1344x768 (16:9)"):
            width, height = 1344, 768
        if(resolution == "1536x640 (21:9)"):
            width, height = 1536, 640


         #path, width, height, batch_size, frame_rate, frame_load_cap, skip_first_frames, select_every_nth
        Path = ""
        if relative_path:
            Path = "./" + new_path
        else:
            Path = os.path.join(self.output_dir, new_path)

        rlist = []
        rlist.append(int(width))
        rlist.append(int(height))
        rlist.append(int(batch_size))
        rlist.append(float(frame_rate))
        rlist.append(int(frame_load_cap))
        rlist.append(int(skip_first_frames))
        rlist.append(int(select_every_nth))
        rlist.append(str(Path))        

        return (rlist,)
       

NODE_NAME = 'Project Folder Video (Pipe) [RvTools]'
NODE_DESC = 'Project Folder Video (Pipe)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvFolders_ProjectFolder_Video_Pipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
