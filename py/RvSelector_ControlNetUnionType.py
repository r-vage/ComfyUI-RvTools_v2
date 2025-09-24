from ..core import CATEGORY

#from the model page: canny (0), tile (1), depth (2), blur (3), pose (4), gray (5), low quality (6)
#https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro

UNION_CONTROLNET_TYPES = {
    "canny/lineart/anime_lineart/mlsd": 0,
    "tile": 1,
    "depth": 2,
    "blur": 3,
    "openpose": 4,
    "gray": 5,
    "low quality": 6,
}

class RvSelector_ControlNetUnionType:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"control_net": ("CONTROL_NET", ),
                             "type": (list(UNION_CONTROLNET_TYPES.keys()),)
                             }}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.SETTINGS.value
    RETURN_TYPES = ("CONTROL_NET",)

    FUNCTION = "set_controlnet_type"

    def set_controlnet_type(self, control_net, type):
        control_net = control_net.copy()
        type_number = UNION_CONTROLNET_TYPES.get(type, -1)
        if type_number >= 0:
            control_net.set_extra_arg("control_type", [type_number])
        else:
            control_net.set_extra_arg("control_type", [])

        return (control_net,)    

NODE_NAME = 'ControlNet Set Union Types (Flux) [RvTools]'
NODE_DESC = 'ControlNet Set Union Types (Flux)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvSelector_ControlNetUnionType
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
