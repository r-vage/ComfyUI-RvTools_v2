from ..core import CATEGORY

class RvPipe_In_Generation_Data_v2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "pipe": ("pipe",),
                "sampler_name": ("STRING",{"forceInput": True, "default": ""}),
                "scheduler": ("STRING",{"forceInput": True, "default": ""}),
                "steps": ("INT", {"forceInput": True, "default": 25}),
                "cfg": ("FLOAT",{"forceInput": True, "default": 6.5}),
                "seed_value": ("INT",{"forceInput": True, "default": 1234}),
                "width": ("INT",{"forceInput": True, "default": 832}),
                "height": ("INT",{"forceInput": True, "default": 1216}),
                "positive": ("STRING",{"forceInput": True, "default": ""}),
                "negative": ("STRING",{"forceInput": True, "default": ""}),
                "modelname": ("STRING",{"forceInput": True, "default": ""}),
                "vae_name": ("STRING",{"forceInput": True, "default": ""}),
                "loras": ("STRING",{"forceInput": True, "default": ""}),
                "denoise": ("FLOAT",{"forceInput": True, "default": 0}),
                "clip_skip": ("INT",{"forceInput": True, "default": 0}),
            },
            "hidden": {
                "pipe_version": ("STRING",{"default": "V2"}),

            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    def execute(self, pipe=None, pipe_version=None, sampler_name=None, scheduler=None, steps=None, cfg=None, seed_value=None, width=None, height=None, positive=None, negative=None, modelname=None, vae_name=None, loras=None, denoise=None, clip_skip=None):
        pipe_version = "V2"
        sampler_name_original = None
        scheduler_original = None
        steps_original = None
        cfg_original = None
        seed_value_original = None
        width_original = None
        height_original = None
        positive_original = None
        negative_original = None
        modelname_original = None
        vae_name_original = None
        loras_original = None
        denoise_original = None
        clip_skip_original = None

        if pipe != None:
           pipe_version, sampler_name_original, scheduler_original, steps_original, cfg_original, seed_value_original, width_original, height_original, positive_original, negative_original, modelname_original, vae_name_original, loras_original, denoise_original, clip_skip_original = pipe

        RBusAnyMod = []

        RBusAnyMod.append(pipe_version)
        RBusAnyMod.append(sampler_name if sampler_name is not None else sampler_name_original)
        RBusAnyMod.append(scheduler if scheduler is not None else scheduler_original)
        RBusAnyMod.append(steps if steps is not None else steps_original)
        RBusAnyMod.append(cfg if cfg is not None else cfg_original)
        RBusAnyMod.append(seed_value if seed_value is not None else seed_value_original)
        RBusAnyMod.append(width if width is not None else width_original)
        RBusAnyMod.append(height if height is not None else height_original)
        RBusAnyMod.append(positive if positive is not None else positive_original)
        RBusAnyMod.append(negative if negative is not None else negative_original)
        RBusAnyMod.append(modelname if modelname is not None else modelname_original)
        RBusAnyMod.append(vae_name if vae_name is not None else vae_name_original)
        RBusAnyMod.append(loras if loras is not None else loras_original)
        RBusAnyMod.append(denoise if denoise is not None else denoise_original)
        RBusAnyMod.append(clip_skip if clip_skip is not None else clip_skip_original)


        return (RBusAnyMod,)

NODE_NAME = 'Pipe In Generation Data II [RvTools]'
NODE_DESC = 'Pipe In Generation Data II'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_In_Generation_Data_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
