import math
from ..core import CATEGORY

#original by mr.pepe69: https://github.com/mr-pepe69/ComfyUI-SelectStringFromListWithIndex

def wrapIndex(index, length):
    if length == 0:
        print("Divide by zero error, returning 0.")
        return 0,0
        
    # Using modulo ensures the index won't go out of range, wrapping back to 0 instead
    # math.fmod returns more predictable results when index is negative
    index_mod = int(math.fmod(index, length))
    wraps = index//length
    return index_mod, wraps

class RvLogic_StringFromList:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "list_input": ("STRING", {"forceInput":True},),
                "index": ("INT", {"default": 0, "min": -999, "max": 999, "step": 1}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.TEXT.value
    RETURN_TYPES = ("STRING", "INT", "INT",)
    RETURN_NAMES = ("list item", "size", "wraps",)
    
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, False, True)

    FUNCTION = "execute"

    def execute(self, list_input, index):
        length = len(list_input)

        wraps_list, item_list = [],[]

        for i in index:
            index_mod, wraps = wrapIndex(i, length)
            wraps_list.append(wraps)
            item_list.append(list_input[index_mod])
            
        return (item_list, length, wraps_list,)

NODE_NAME = 'String from List [RvTools]'
NODE_DESC = 'String from List '

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvLogic_StringFromList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
