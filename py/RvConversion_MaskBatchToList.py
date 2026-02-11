import torch  # type: ignore

from ..core import CATEGORY, make_3d_mask, log


class RvConversion_MaskBatchToList:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                        "masks": ("MASK", ),
                      }
                }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("MASK", )
    OUTPUT_IS_LIST = (True, )

    FUNCTION = "execute"

    def execute(self, masks):
        if masks is None:
            empty_mask = torch.zeros((64, 64), dtype=torch.float32, device="cpu")
            return ([empty_mask], )

        res = []

        for mask in masks:
            res.append(mask)

        log.info("MaskBatchToList", f"mask len: {len(res)}")

        res = [make_3d_mask(x) for x in res]

        return (res, )

NODE_NAME = 'Maskbatch to List [RvTools]'
NODE_DESC = 'Maskbatch to List'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_MaskBatchToList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
