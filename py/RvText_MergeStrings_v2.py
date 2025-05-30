from ..core import CATEGORY

class RvText_MergeStrings_2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            },
            "optional": {
                "string_1": ("STRING", {"forceInput": True, "default": ""}),
                "string_2": ("STRING", {"forceInput": True, "default": ""}),
                "string_3": ("STRING", {"forceInput": True, "default": ""}),
                "string_4": ("STRING", {"forceInput": True, "default": ""}),
                "string_5": ("STRING", {"forceInput": True, "default": ""}),
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

NODE_NAME = 'Merge Strings v2 [RvTools]'
NODE_DESC = 'Merge Strings v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvText_MergeStrings_2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
