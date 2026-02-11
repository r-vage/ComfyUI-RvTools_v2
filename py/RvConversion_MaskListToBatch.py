import torch  # type: ignore
import comfy  # type: ignore

from ..core import CATEGORY

def make_3d_mask(mask):
    if len(mask.shape) == 4:
        return mask.squeeze(0)

    elif len(mask.shape) == 2:
        return mask.unsqueeze(0)

    return mask

class RvConversion_MaskListToBatch:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                        "mask": ("MASK", ),
                      }
                }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("MASK", )
    INPUT_IS_LIST = True

    FUNCTION = "execute"

    def execute(self, mask):
        if len(mask) == 1:
            mask = make_3d_mask(mask[0])
            return (mask,)
        elif len(mask) > 1:
            mask1 = make_3d_mask(mask[0])

            for mask2 in mask[1:]:
                mask2 = make_3d_mask(mask2)
                if mask1.shape[1:] != mask2.shape[1:]:
                    mask2 = comfy.utils.common_upscale(mask2.movedim(-1, 1), mask1.shape[2], mask1.shape[1], "lanczos", "center").movedim(1, -1)
                mask1 = torch.cat((mask1, mask2), dim=0)

            return (mask1,)
        else:
            empty_mask = torch.zeros((1, 64, 64), dtype=torch.float32, device="cpu").unsqueeze(0)
            return (empty_mask,)

NODE_NAME = 'Masklist to Batch [RvTools]'
NODE_DESC = 'Masklist to Batch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_MaskListToBatch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}