import math
from ..core import CATEGORY, log

#original by mr.pepe69: https://github.com/mr-pepe69/ComfyUI-SelectStringFromListWithIndex

def wrapIndex(index, length):
    """
    Calculate wrapped index and number of wraps
    """
    if length <= 0:
        log.warning("StringFromList", "Invalid list length, returning 0.")
        return 0, 0
        
    # Convert to integer and handle wrap-around
    index = int(index)
    index_mod = ((index % length) + length) % length  # Handles negative indices correctly
    wraps = index // length if length > 0 else 0
    return index_mod, wraps

class RvLogic_StringFromList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "list_input": ("STRING", {"forceInput": True}),
                "index": ("INT", {"default": 0, "min": -999, "max": 999, "step": 1}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.TEXT.value
    RETURN_TYPES = ("STRING", "INT", "INT")
    RETURN_NAMES = ("list item", "size", "wraps")
    
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, False, True)

    FUNCTION = "execute"

    def execute(self, list_input, index):
        try:
            # Ensure list_input is not empty
            if not list_input:
                log.warning("StringFromList", "Empty input list, returning empty results")
                return ([], 0, [])

            length = len(list_input)
            wraps_list = []
            item_list = []

            # Handle single index or list of indices
            indices = index if isinstance(index, list) else [index]
            
            for i in indices:
                index_mod, wraps = wrapIndex(i, length)
                # Ensure index is within bounds
                if 0 <= index_mod < length:
                    wraps_list.append(wraps)
                    item_list.append(list_input[index_mod])
                else:
                    log.warning("StringFromList", f"Index {i} out of range for list of length {length}")
                    wraps_list.append(0)
                    item_list.append("")

            return (item_list, length, wraps_list)

        except Exception as e:
            log.error("StringFromList", f"Error in StringFromList: {str(e)}")
            return ([], 0, [])

NODE_NAME = 'String from List [RvTools]'
NODE_DESC = 'String from List '

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvLogic_StringFromList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
