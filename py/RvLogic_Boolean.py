from ..core import CATEGORY


class RvLogic_Boolean:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": ("BOOLEAN", {"default": True}),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("boolean",)

    FUNCTION = "execute"

    def execute(self, value=True):
        return (value,)

NODE_NAME = 'Boolean [RvTools]'
NODE_DESC = 'Boolean'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvLogic_Boolean
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
