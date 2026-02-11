import os
import sys
import random
import torch  # type: ignore
import numpy as np
import folder_paths  # type: ignore
import safetensors.torch

from PIL import Image, ImageOps, ImageSequence, ImageFile
from PIL.PngImagePlugin import PngInfo

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

from ..core import CATEGORY

class RvImage_PreviewImage():
    def __init__(self):
        self.output_dir = folder_paths.get_temp_directory()
        self.type = "temp"
        self.prefix_append = "_temp_" + ''.join(random.choice("abcdefghijklmnopqrstupvxyz") for x in range(5))
        self.compress_level = 1

    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                        "images": ("IMAGE", ), 
                        "Show_Images": ("INT", {"default": -1,"min": -1,"max": sys.maxsize,"step": 1}), 
                    },
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.IMAGE.value

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"
    OUTPUT_NODE = True

    def execute(self, images, filename_prefix="ComfyUI", Show_Images=0, prompt=None, extra_pnginfo=None):
        filename_prefix += self.prefix_append
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir, images[0].shape[1], images[0].shape[0])
        results = list()

        for (batch_number, image) in enumerate(images):
            if Show_Images == 0: break # no preview for whatever reason

            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = None

            filename_with_batch_num = filename.replace("%batch_num%", str(batch_number))
            file = f"{filename_with_batch_num}_{counter:05}_.png"
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=self.compress_level)
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": self.type
            })
            

            if Show_Images > -1: #-1 will display all images
               if (batch_number + 1) == Show_Images:
                break 

            counter += 1

        return { "ui": { "images": results }, "result": (images,) }

NODE_NAME = 'Preview Image [RvTools]'
NODE_DESC = 'Preview Image'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvImage_PreviewImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
