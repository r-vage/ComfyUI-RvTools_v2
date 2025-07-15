from ..core import CATEGORY

class RvPipe_Out_CheckpointLoader_Small:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"pipe": ("pipe",),}}

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = ("pipe", "MODEL", "CLIP", "VAE", "INT",        "STRING",     "STRING",)
    RETURN_NAMES = ("pipe", "model", "clip", "vae", "batch_size", "model_name", "vae_name",)

    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, pipe=None, ):
        model, clip, vae, latent, width, height, batch_size, modelname, vae_name = pipe
        
        return pipe, model, clip, vae, batch_size, modelname, vae_name

NODE_NAME = 'Pipe Out Checkpoint Loader Small + v3 [RvTools]'
NODE_DESC = 'Pipe Out Checkpoint Loader Small + v3'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_Out_CheckpointLoader_Small
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
