from ..core import CATEGORY

class RvSettings_WvW_Setup:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "steps": ("INT", {"default": 4, "min": 1}),
                "cfg": ("FLOAT", {"default": 1.0, "min": 1.0}),
                "model_shift": ("FLOAT", {"default": 5.0, "min": 0}),
                "split_steps_start": ("INT", {"default": 2, "min": -1}),
                "split_steps_end": ("INT", {"default": 2, "min": -1, "max": 10000}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"
    
    def execute(self, steps, cfg, model_shift, split_steps_start, split_steps_end):
        
            
        rlist = []
        rlist.append(int(steps))
        rlist.append(int(cfg))
        rlist.append(int(model_shift))
        rlist.append(int(split_steps_start))
        rlist.append(int(split_steps_end))

        return (rlist,)

NODE_NAME = 'WanVideo Setup [RvTools]'
NODE_DESC = 'WanVideo Setup'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_WvW_Setup
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
