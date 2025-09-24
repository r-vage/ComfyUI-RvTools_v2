from ..core import CATEGORY

class RvSettings_Resolution_SD15:
    resolution =     ["512x512 (1:1)",              
                      "512x682 (3:4)",
                      "512x768 (2:3)",
                      "512x910 (9:16)",
                      "512x952 (1:1.85)",
                      "512x1024 (1:2)",
                      "512x1224 (1:2.39)",
                      "682x512 (4:3)",
                      "768x512 (3:2)",
                      "910x512 (16:9)",
                      "952x512 (1.85:1)",
                      "1024x512 (2:1)",
                      "1224x512 (2.39:1)"
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
        
        if(resolution == "512x512 (1:1)"):
            width, height = 512, 512
        if(resolution == "512x682 (3:4)"):
            width, height = 512, 682
        if(resolution == "512x768 (2:3)"):
            width, height = 512, 768
        if(resolution == "512x910 (9:16)"):
            width, height = 512, 910
        if(resolution == "512x952 (1:1.85)"):
            width, height = 512, 952
        if(resolution == "512x1024 (1:2)"):
            width, height = 512, 1024
        if(resolution == "512x1224 (1:2.39)"):
            width, height = 512, 1224
        if(resolution == "682x512 (4:3)"):
            width, height = 682, 512
        if(resolution == "768x512 (3:2)"):
            width, height = 768, 512
        if(resolution == "910x512 (16:9)"):
            width, height = 910, 512
        if(resolution == "952x512 (1.85:1)"):
            width, height = 952, 512
        if(resolution == "1024x512 (2:1)"):
            width, height = 1024, 512
        if(resolution == "1224x512 (2.39:1)"):
            width, height = 1224, 512
            
        return(int(width),int(height))

NODE_NAME = 'Aspect Ratio (SD15) [RvTools]'
NODE_DESC = 'Aspect Ratio (SD15)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSettings_Resolution_SD15
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
