from ..core import CATEGORY

#created for seamless_join_video_clips & combine_video_clips

class RvSettings_FilenameConstruct:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": ""}),
                "filename_prefix": ("STRING", {"default": "vc"}),
                "filename_suffix": ("INT", {"default": 1, "min": 1,}),
                "number_padding": ("INT", {"default": 4}),
                "file_extension": ("STRING", {"default": ".mp4"}),
                "mask_frames_last": ("INT", {"default": 0}),
                "mask_frames_first": ("INT", {"default": 10}),
                "frame_load_cap": ("INT", {"default": 81}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, path, filename_prefix, filename_suffix, number_padding, file_extension, mask_frames_last, mask_frames_first, frame_load_cap):
        rList = list()
        Filename = ""
        Padding = ""
        counter = filename_suffix

        rList.append(mask_frames_last)    
        rList.append(mask_frames_first)    
        rList.append(frame_load_cap)    

        for _ in range (1, 6) :
            Filename = path + "\\" + filename_prefix + "_" + Padding.zfill(number_padding) + str(counter) + file_extension
            rList.append(Filename)
            
            counter += 1

        counter = filename_suffix
        for _ in range (1, 6) :
            Filename = path + "\\" + filename_prefix + "_join_" + Padding.zfill(number_padding) + str(counter) + file_extension
            rList.append(Filename)
            
            counter += 1

        return (rList,)

NODE_NAME = 'Filename Construct [RvTools]'
NODE_DESC = 'Filename Construct'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_FilenameConstruct
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
