import torch  # type: ignore
import numpy as np

from PIL import Image

from ..core import CATEGORY, tensor2pil, pil2tensor


class RvConversion_ImagesToRGB:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)

    FUNCTION = "execute"

    def execute(self, images):

        if len(images) > 1:
            tensors = []
            for image in images:
                tensors.append(pil2tensor(tensor2pil(image).convert('RGB')))
            tensors = torch.cat(tensors, dim=0)
            return (tensors, )
        else:
            return (pil2tensor(tensor2pil(images).convert("RGB")), )

NODE_NAME = 'Image to RGB [RvTools]'
NODE_DESC = 'Image to RGB'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_ImagesToRGB
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}