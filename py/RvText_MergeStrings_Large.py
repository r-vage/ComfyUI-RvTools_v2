from ..core import CATEGORY
from ..core import AnyType

any = AnyType("*")

class RvText_MergeStrings_Large:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "any_1": (any, {"default": ""}),
                "any_2": (any, {"default": ""}),
                "any_3": (any, {"default": ""}),
                "any_4": (any, {"default": ""}),
                "any_5": (any, {"default": ""}),
                "any_6": (any, {"default": ""}),
                "any_7": (any, {"default": ""}),
                "any_8": (any, {"default": ""}),
                "any_9": (any, {"default": ""}),
                "any_10": (any, {"default": ""}),

                "Delimiter": ("STRING", {"default": ", "}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.TEXT.value
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "execute"

    def execute(self, Delimiter, **kwargs):

        text_inputs = []

        # Handle special case where delimiter is "\n" (literal newline).
        if Delimiter in ("\n", "\\n"):
            Delimiter = "\n"

        # Iterate over the received inputs in sorted order.
        for k in sorted(kwargs.keys()):
            v = kwargs[k]

            # Only process string input ports.
            if isinstance(v, str):
               if v != "":
                  text_inputs.append(v)

        merged_text = Delimiter.join(text_inputs)

        return (merged_text,)

NODE_NAME = 'Merge Strings (Large) [RvTools]'
NODE_DESC = 'Merge Strings (Large)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvText_MergeStrings_Large
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
