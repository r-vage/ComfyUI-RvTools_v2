from ..core import CATEGORY

class RvSettings_Resolution_All:
    resolution =     ["SD15 - 512x512 (1:1)",              
                      "SD15 - 512x682 (3:4)",
                      "SD15 - 512x768 (2:3)",
                      "SD15 - 512x910 (9:16)",
                      "SD15 - 512x952 (1:1.85)",
                      "SD15 - 512x1024 (1:2)",
                      "SD15 - 512x1224 (1:2.39)",
                      "SD15 - 682x512 (4:3)",
                      "SD15 - 768x512 (3:2)",
                      "SD15 - 910x512 (16:9)",
                      "SD15 - 952x512 (1.85:1)",
                      "SD15 - 1024x512 (2:1)",
                      "SD15 - 1224x512 (2.39:1)",
                      "SDXL - 640x1536 (9:21)",
                      "SDXL - 768x1344 (9:16)",
                      "SDXL - 832x1216 (2:3)",
                      "SDXL - 896x1152 (3:4)",
                      "SDXL - 1024x1024 (1:1)",
                      "SDXL - 1152x896 (4:3)",
                      "SDXL - 1216x832 (3:2)",
                      "SDXL - 1344x768 (16:9)",
                      "SDXL - 1536x640 (21:9)" 
                      ]

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"resolution": (s.resolution,),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.IMAGE.value
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("width", "height")

    FUNCTION = "execute"


    def execute(self,resolution):
        width = 512
        height = 512
        width = int(width)
        height = int(height)
        
        if(resolution == "SD15 - 512x512 (1:1)"):
            width, height = 512, 512
        if(resolution == "SD15 - 512x682 (3:4)"):
            width, height = 512, 682
        if(resolution == "SD15 - 512x768 (2:3)"):
            width, height = 512, 768
        if(resolution == "SD15 - 512x910 (9:16)"):
            width, height = 512, 910
        if(resolution == "SD15 - 512x952 (1:1.85)"):
            width, height = 512, 952
        if(resolution == "SD15 - 512x1024 (1:2)"):
            width, height = 512, 1024
        if(resolution == "SD15 - 512x1224 (1:2.39)"):
            width, height = 512, 1224
        if(resolution == "SD15 - 682x512 (4:3)"):
            width, height = 682, 512
        if(resolution == "SD15 - 768x512 (3:2)"):
            width, height = 768, 512
        if(resolution == "SD15 - 910x512 (16:9)"):
            width, height = 910, 512
        if(resolution == "SD15 - 952x512 (1.85:1)"):
            width, height = 952, 512
        if(resolution == "SD15 - 1024x512 (2:1)"):
            width, height = 1024, 512
        if(resolution == "SD15 - 1224x512 (2.39:1)"):
            width, height = 1224, 512

        if(resolution == "SDXL - 640x1536 (9:21)"):
            width, height = 640, 1536
        if(resolution == "SDXL - 768x1344 (9:16)"):
            width, height = 768, 1344
        if(resolution == "SDXL - 832x1216 (2:3)"):
            width, height = 832, 1216
        if(resolution == "SDXL - 896x1152 (3:4)"):
            width, height = 896, 1152
        if(resolution == "SDXL - 1024x1024 (1:1)"):
            width, height = 1024, 1024
        if(resolution == "SDXL - 1152x896 (4:3)"):
            width, height = 1152, 896
        if(resolution == "SDXL - 1216x832 (3:2)"):
            width, height = 1216, 832
        if(resolution == "SDXL - 1344x768 (16:9)"):
            width, height = 1344, 768
        if(resolution == "SDXL - 1536x640 (21:9)"):
            width, height = 1536, 640
            
        return(int(width),int(height))

NODE_NAME = 'Aspect Ratio (All) [RvTools]'
NODE_DESC = 'Aspect Ratio (All)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Resolution_All
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
