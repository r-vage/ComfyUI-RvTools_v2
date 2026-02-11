import torch  # type: ignore
import torchvision.transforms.v2 as T

from ..core import CATEGORY

def p(image):
    return image.permute([0,3,1,2])
def pb(image):
    return image.permute([0,2,3,1])


class RvConversion_ImageListToBatch:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CONVERSION.value
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    INPUT_IS_LIST = True

    FUNCTION = "execute"

    def execute(self, images):
        shape = images[0].shape[1:3]
        out = []

        for i in range(len(images)):
            img = p(images[i])
            if images[i].shape[1:3] != shape:
                transforms = T.Compose([
                    T.CenterCrop(min(img.shape[2], img.shape[3])),
                    T.Resize((shape[0], shape[1]), interpolation=T.InterpolationMode.BICUBIC),
                ])
                img = transforms(img)
            out.append(pb(img))
            #image[i] = pb(transforms(img))

        out = torch.cat(out, dim=0)

        return (out,)

NODE_NAME = 'Imagelist to Batch [RvTools]'
NODE_DESC = 'Imagelist to Batch'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvConversion_ImageListToBatch
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}