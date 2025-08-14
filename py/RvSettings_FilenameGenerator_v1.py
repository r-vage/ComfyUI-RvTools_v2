import json
import os
import folder_paths

from ..core import CATEGORY, cstr

#created for seamless_join_video_clips & combine_video_clips
#v1 is used for combine only it automaticly sets the 2nd filename (filename_suffix_start +1), it also provides the mask settings

class RvSettings_FilenameGenerator_v1:
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
                "filename_suffix_start": ("INT", {"default": 1, "min": 1, "max": 0xffffffffffffffff, "control_after_generate": True,}),
                "file_extension": ("STRING", {"default": ".mp4"}),
                "frame_load_cap": ("INT", {"default": 81}),
                "mask_first_frames": ("INT", {"default": 10}),                
                "mask_last_frames": ("INT", {"default": 0}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, path, filename_prefix, filename_suffix_start, file_extension, frame_load_cap, mask_first_frames, mask_last_frames):
        if not path:
            raise ValueError(f"Path is missing. Enter the Path to your Video Files.")                    
        else:
            rList = list()
            Filename = ""

            rList.append(path)    
            rList.append(frame_load_cap)    
            rList.append(mask_first_frames)
            rList.append(mask_last_frames)    

            counter = filename_suffix_start
            
            fDict = {}
            flist = list()

            for _ in range (filename_suffix_start, filename_suffix_start+2) :
                number = str(counter)
        
                Filename = path + "\\" + filename_prefix + "_" + number.zfill(5) + file_extension
                flist.append(Filename)
                counter += 1
            
            fDict["FILE"] = flist

            rList.append(fDict)

            return (rList,)

NODE_NAME = 'VC-Filename Generator I [RvTools]'
NODE_DESC = 'VC-Filename Generator I'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_FilenameGenerator_v1
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
