import comfy
import comfy.sd
import torch
import folder_paths

from ..core import CATEGORY

MAX_RESOLUTION = 32768

class RvCheckpointLoader_v1_Pipe:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"),),
                "vae_name": (["Baked VAE"] + folder_paths.get_filename_list("vae"),),
                "Baked_Clip": ("BOOLEAN", {"default": True},),
                "Use_Clip_Layer": ("BOOLEAN", {"default": True},),
                "stop_at_clip_layer": ("INT", {"default": -2, "min": -24, "max": -1, "step": 1},),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CHECKPOINT.value

    RETURN_TYPES = ("pipe",)
    FUNCTION = "execute"

    def execute(self, ckpt_name, vae_name, Baked_Clip, Use_Clip_Layer, stop_at_clip_layer):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        output_vae = (vae_name == "Baked VAE")

        loaded_ckpt = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=output_vae, output_clip=Baked_Clip, embedding_directory=folder_paths.get_folder_paths("embeddings"),)

        vae_path = ""

        if vae_name == "Baked VAE":
            loaded_vae = loaded_ckpt[:3][2]
        else:
            vae_path = folder_paths.get_full_path("vae", vae_name)
            loaded_vae = comfy.sd.VAE(sd=comfy.utils.load_torch_file(vae_path))

        if Baked_Clip:
            loaded_clip = loaded_ckpt[:3][1].clone()
            if Use_Clip_Layer: loaded_clip.clip_layer(stop_at_clip_layer)
        else:
            loaded_clip = None

        #model, clip, vae, latent, width, height, batch_size, modelname, vae_name = pipe

        rlist = []
        rlist.append(loaded_ckpt[:3][0])
        rlist.append(loaded_clip)
        rlist.append(loaded_vae)

        rlist.append(None)              #latent
        rlist.append(int(8))            #width
        rlist.append(int(8))            #height 
        rlist.append(int(1))            #batchsize

        rlist.append(str(ckpt_name))   #model_name without path

        if vae_name == "Baked VAE":
           rlist.append('')             #empty string no file selected
        else:
            rlist.append(str(vae_name)) #vae_name (no path)


        return (rlist,)

NODE_NAME = 'Checkpoint Loader v1 (Pipe) [RvTools]'
NODE_DESC = 'Checkpoint Loader v1 (Pipe)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvCheckpointLoader_v1_Pipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
