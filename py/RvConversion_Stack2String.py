from ..core import CATEGORY

# TSC LoRA Stack to String converter
class RvConversion_Stack2String:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"lora_stack": ("LORA_STACK",)}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("LoRA string",)
    FUNCTION = "convert"
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value

    def convert(self, lora_stack):
        """
        Converts a list of tuples into a single space-separated string.
        Each tuple contains (STR, FLOAT1, FLOAT2) and is converted to the format "<lora:STR:FLOAT1:FLOAT2>".
        """
        output = ' '.join(f"<lora:{tup[0]}:{tup[1]}:{tup[2]}>" for tup in lora_stack)
        return (output,)

NODE_NAME = 'Lora Stack to String [RvTools]'
NODE_DESC = 'Lora Stack to String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_Stack2String
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}

