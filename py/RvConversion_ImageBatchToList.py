from ..core import CATEGORY

class RvConversion_ImageBatchToList:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"images": ("IMAGE",), }}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    OUTPUT_IS_LIST = (True,)
    
    FUNCTION = "execute"

    def execute(self, images):
        img = [images[i:i + 1, ...] for i in range(images.shape[0])]
        return (img, )

NODE_NAME = 'Imagebatch to List [RvTools]'
NODE_DESC = 'Imagebatch to List'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_ImageBatchToList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}