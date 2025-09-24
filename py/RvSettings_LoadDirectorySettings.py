from ..core import CATEGORY

class RvSettings_LoadDirectorySettings:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Directory": ("STRING", {"default": ""}),
                "start_index": ("INT", {"default": 0, "min": 0, "control_after_generate": True,}),
                "loadcap": ("INT", {"default": 20}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, Directory, start_index, loadcap):
        rlist = []
        rlist.append(str(Directory))
        rlist.append(int(start_index))
        rlist.append(int(loadcap))

        return (rlist,)

NODE_NAME = 'Load Directory Settings [RvTools]'
NODE_DESC = 'Load Directory Settings'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_LoadDirectorySettings
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
