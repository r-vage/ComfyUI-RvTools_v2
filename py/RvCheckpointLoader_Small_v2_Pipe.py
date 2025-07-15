import comfy
import comfy.sd
import torch
import folder_paths

from ..core import CATEGORY

MAX_RESOLUTION = 32768

class RvCheckpointLoader_Small_v2_Pipe:
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

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value

    RETURN_TYPES = ("pipe",)
    FUNCTION = "execute"
    DEPRECATED = True

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

        #model, clip, vae, batch_size, modelname, vae_name = pipe

        rlist = []
        rlist.append(loaded_ckpt[:3][0])
        rlist.append(loaded_clip)
        rlist.append(loaded_vae)
        
        rlist.append(None)              #latent
        rlist.append(int(8))            #width
        rlist.append(int(8))            #height 
        rlist.append(int(1))            #batchsize

        rlist.append(str(ckpt_name))      #str(ckpt_path)) #model_name

        if vae_name == "Baked VAE":
           rlist.append('')             #empty string no file selected
        else:
            rlist.append(str(vae_name)) #vae_name (no path)


        return (rlist,)

NODE_NAME = 'Checkpoint Loader Small v2 (Pipe) [RvTools]'
NODE_DESC = 'Checkpoint Loader Small v2 (Pipe)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvCheckpointLoader_Small_v2_Pipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
