import json

from ..core import CATEGORY

#created for seamless_join_video_clips & combine_video_clips

class RvSettings_FilenameGenerator:
    def __init__(self):
        pass

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
                "mask_last_frames": ("INT", {"default": 0}),
                "mask_first_frames": ("INT", {"default": 10}),

            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, path, filename_prefix, filename_suffix_start, filename_suffix_end, join_suffix_start, simple_combine, file_extension, frame_load_cap, mask_last_frames, mask_first_frames):
        if not path:
            raise ValueError(f"Path is missing. Enter the Path to your Video Files.")                    
        else:
            rList = list()
            Filename = ""

            rList.append(frame_load_cap)    
            rList.append(mask_last_frames)    
            rList.append(mask_first_frames)    
            rList.append(simple_combine)    

            counter = filename_suffix_start
            
            fDict = {}
            flist = list()

            for _ in range (filename_suffix_start, filename_suffix_end + 1) :
                number = str(counter)
        
                Filename = path + "\\" + filename_prefix + "_" + number.zfill(5) + file_extension
                flist.append(Filename)
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
                counter += 1
            
            jDict["JOIN"] = jlist
            rList.append(jDict)

            return (rList,)

NODE_NAME = 'VC-Filename Generator [RvTools]'
NODE_DESC = 'VC-Filename Generator'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_FilenameGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
