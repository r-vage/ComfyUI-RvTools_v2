import os
from ..core import CATEGORY


class RvFolders_AddFolder:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"forceInput": True}),
                "folder_name": ("STRING", {"multiline": False, "default": "SubFolder"})
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.FOLDER.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)    
    
    FUNCTION = "execute"

    def execute(self, path, folder_name):
        new_path = os.path.join(path, folder_name)
        return (new_path,)

NODE_NAME = 'Add Folder [RvTools]'
NODE_DESC = 'Add Folder'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvFolders_AddFolder
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
