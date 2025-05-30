from ..core import CATEGORY

class RvSettings_VHS_InputSettings:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "load_cap": ("INT", {"default": 20, "min": 0}),
                "skip_first_frames": ("INT", {"default": 0, "min": 0}),
                "select_every_nth": ("INT", {"default": 1, "min": 1}),
                "overlap": ("INT", {"default": 0, "min": 0}),
                "images_in_previews": ("INT", {"default": 10, "min": 1}),
                "images_in_filter_previews": ("INT", {"default": 1, "min": 1}),
                "preview_crop_pos": (["center","top", "bottom", "left", "right"],),
                "crop_interpolation": (["lanczos", "nearest", "bilinear", "bicubic", "area", "nearest-exact"],),
                "frame_rate": ("FLOAT", {"default": 30, "min": 1}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"
    
    def execute(self, load_cap, skip_first_frames, select_every_nth, overlap, images_in_previews, images_in_filter_previews, preview_crop_pos,
                crop_interpolation, frame_rate):
        
            
        rlist = []
        rlist.append(int(load_cap))
        rlist.append(int(skip_first_frames))
        rlist.append(int(select_every_nth))
        rlist.append(int(overlap))
        rlist.append(int(images_in_previews))
        rlist.append(int(images_in_filter_previews))
        rlist.append(preview_crop_pos)
        rlist.append(crop_interpolation)
        rlist.append(float(frame_rate))


        return (rlist,)

NODE_NAME = 'VHS Input Settings [RvTools]'
NODE_DESC = 'VHS Input Settings'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_VHS_InputSettings
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
