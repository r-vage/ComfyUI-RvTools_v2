import json
import os
import folder_paths

from ..core import CATEGORY, cstr

#created for seamless_join_video_clips & combine_video_clips
#v2 is used for join only it generates the list from/to
class RvSettings_FilenameGenerator_v2:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        pass

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")  # Always execute to ensure fresh processing

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": ""}),
                "filename_prefix": ("STRING", {"default": "vc"}),
                "filename_suffix_start": ("INT", {"default": 1, "min": 1,}),
                "filename_suffix_end": ("INT", {"default": 5, "min": 1,}),
                "join_suffix_start": ("INT", {"default": 1, "min": 1,}),
                "simple_combine": ("BOOLEAN", {"default": False}),
                "file_extension": ("STRING", {"default": ".mp4"}),
                "frame_load_cap": ("INT", {"default": 81}),

            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, path, filename_prefix, filename_suffix_start, filename_suffix_end, join_suffix_start, simple_combine, file_extension, frame_load_cap):
        if not path:
            raise ValueError(f"Path is missing. Enter the Path to your Video Files.")                    
        else:
            rList = list()
            Filename = ""

            rList.append(path)    
            rList.append(frame_load_cap)    
            rList.append(simple_combine)    

            counter = filename_suffix_start
            
            fDict = {}
            flist = list()

            for _ in range (filename_suffix_start, filename_suffix_end + 1) :
                number = str(counter)
        
                Filename = path + "\\" + filename_prefix + "_" + number.zfill(5) + file_extension
                flist.append(Filename)
                #cstr(f"File added {Filename}").msg.print()
                counter += 1
            
            fDict["FILE"] = flist

            rList.append(fDict)

            join_end_idx = join_suffix_start + len(flist)
            counter = join_suffix_start
            jDict = {}
            jlist = list()

            for _ in range (join_suffix_start, join_end_idx) :
                number = str(counter)
                Filename = path + "\\" + filename_prefix + "_join_" + number.zfill(5) + file_extension
                jlist.append(Filename)
                #cstr(f"Join-File added {Filename}").msg.print()
                counter += 1
            
            jDict["JOIN"] = jlist
            rList.append(jDict)

            return (rList,)

NODE_NAME = 'VC-Filename Generator II [RvTools]'
NODE_DESC = 'VC-Filename Generator II'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_FilenameGenerator_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
