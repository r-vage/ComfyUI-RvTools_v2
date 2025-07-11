from ..core import CATEGORY

class RvPipe_In_CheckpointLoader_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "pipe": ("pipe",),
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
                "latent": ("LATENT",),
                "width": ("INT",{"forceInput": True}),
                "height": ("INT",{"forceInput": True}),
                "batch_size": ("INT",{"forceInput": True}),
                "modelname": ("STRING",{"forceInput": True}),
                "vae_name": ("STRING",{"forceInput": True}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.CHECKPOINT.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, pipe=None, model=None, clip=None, vae=None, latent=None, width=None, height=None, batch_size=None, modelname=None, vae_name=None):
        model_original = None
        clip_original = None
        vae_original = None
        latent_original = None
        width_original = None
        height_original = None
        batch_size_original = None
        modelname_original = None
        vae_name_original = None

        if pipe != None:
            model_original, clip_original, vae_original, latent_original, width_original, height_original, batch_size_original, modelname_original, vae_name_original = pipe

        RBusAnyMod = []

        RBusAnyMod.append(model if model is not None else model_original)
        RBusAnyMod.append(clip if clip is not None else clip_original)
        RBusAnyMod.append(vae if vae is not None else vae_original)
        RBusAnyMod.append(latent if latent is not None else latent_original)
        RBusAnyMod.append(width if width is not None else width_original)
        RBusAnyMod.append(height if height is not None else height_original)
        RBusAnyMod.append(batch_size if batch_size is not None else batch_size_original)
        RBusAnyMod.append(modelname if modelname is not None else modelname_original)
        RBusAnyMod.append(vae_name if vae_name is not None else vae_name_original)

        return (RBusAnyMod,)

NODE_NAME = 'Pipe In Checkpoint Loader v2 [RvTools]'
NODE_DESC = 'Pipe In Checkpoint Loader v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_In_CheckpointLoader_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
