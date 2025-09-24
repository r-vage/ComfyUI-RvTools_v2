from ..core import CATEGORY

class RvPasser_Controlnet:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"control_net": ("CONTROL_NET",),},}
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PASSER.value
    RETURN_TYPES = ("CONTROL_NET",)
    FUNCTION = "passthrough"

    def passthrough(self, control_net):
        return control_net,

NODE_NAME = 'Pass ControlNet [RvTools]'
NODE_DESC = 'Pass ControlNet'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPasser_Controlnet
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
