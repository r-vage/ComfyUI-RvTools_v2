from ..core import CATEGORY

class RvText_Multiline:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PRIMITIVE.value
    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("string", "string_list",)

    OUTPUT_IS_LIST = (False, True)

    FUNCTION = "execute"

    def execute(self, string=None):
        try:
            # Handle None or empty input
            if not string or string.isspace():
                return ("", [""])

            # Strip and split the input
            string = string.strip()
            string_list = string.split('\n')
            
            # Filter out empty lines and strip whitespace
            string_list = [line.strip() for line in string_list if line.strip()]
            
            # If no valid lines found, return empty
            if not string_list:
                return ("", [""])
            
            # For single line, return it for both outputs
            if len(string_list) == 1:
                return (string_list[0], [string_list[0]])
            
            # For multiple lines, return first line and full list
            return (string_list[0], string_list)

        except Exception as e:
            print(f"Error in RvText_Multiline: {str(e)}")
            return ("", [""])

NODE_NAME = 'String Multiline with List [RvTools]'
NODE_DESC = 'String Multiline with List'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvText_Multiline
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
