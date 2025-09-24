from ..core import CATEGORY

class RvSettings_Resolution_SDXL:
    resolution =     ["640x1536 (9:21)",
                      "768x1344 (9:16)",
                      "832x1216 (2:3)",
                      "896x1152 (3:4)",
                      "1024x1024 (1:1)",
                      "1152x896 (4:3)",
                      "1216x832 (3:2)",
                      "1344x768 (16:9)",
                      "1536x640 (21:9)" 
                      ]

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "resolution": (s.resolution,),
            }
        }
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.IMAGE.value
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("width", "height")

    FUNCTION = "execute"


    def execute(self,resolution):
        width = 1024
        height = 1024
        width = int(width)
        height = int(height)
        
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
            
        return(int(width),int(height))

NODE_NAME = 'Aspect Ratio (SDXL) [RvTools]'
NODE_DESC = 'Aspect Ratio (SDXL)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Resolution_SDXL
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
