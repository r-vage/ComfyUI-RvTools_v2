import comfy
import comfy.sd
import torch
import folder_paths

from ..core import CATEGORY

MAX_RESOLUTION = 32768

class RvCheckpointLoader_Small:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"),),
                "vae_name": (["Baked VAE"] + folder_paths.get_filename_list("vae"),),
                "stop_at_clip_layer": ("INT", {"default": -1, "min": -24, "max": -1, "step": 1},),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CHECKPOINT.value

    RETURN_TYPES = ("MODEL", "VAE", "CLIP", "STRING",)
    RETURN_NAMES = ("model", "vae", "clip", "model_name")
    FUNCTION = "execute"

    def execute(self, ckpt_name, vae_name, stop_at_clip_layer):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)

        output_vae = (vae_name == "Baked VAE")

        loaded_ckpt = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=output_vae, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"),)

        vae_path = ""

        if vae_name == "Baked VAE":
            loaded_vae = loaded_ckpt[:3][2]
        else:
            vae_path = folder_paths.get_full_path("vae", vae_name)
            loaded_vae = comfy.sd.VAE(sd=comfy.utils.load_torch_file(vae_path))

        loaded_clip = loaded_ckpt[:3][1].clone()
        loaded_clip.clip_layer(stop_at_clip_layer)

        return (loaded_ckpt[:3][0], loaded_vae, loaded_clip, ckpt_name,)

NODE_NAME = 'Checkpoint Loader Small [RvTools]'
NODE_DESC = 'Checkpoint Loader Small'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvCheckpointLoader_Small
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
