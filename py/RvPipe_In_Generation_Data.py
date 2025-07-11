from ..core import CATEGORY

class RvPipe_In_Generation_Data:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "pipe": ("pipe",),
                "steps": ("INT", {"forceInput": True}),
                "cfg": ("FLOAT",{"forceInput": True}),
                "sampler_name": ("STRING",{"forceInput": True}),
                "scheduler": ("STRING",{"forceInput": True}),
                "positive": ("STRING",{"forceInput": True, "default": ""}),
                "negative": ("STRING",{"forceInput": True, "default": ""}),
                "modelname": ("STRING",{"forceInput": True, "default": ""}),
                "width": ("INT",{"forceInput": True}),
                "height": ("INT",{"forceInput": True}),
                "seed_value": ("INT",{"forceInput": True}),
                "loras": ("STRING",{"forceInput": True, "default": ""}),
                "vae_name": ("STRING",{"forceInput": True, "default": ""}),
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value
    RETURN_TYPES = ("pipe",)

    FUNCTION = "execute"

    #steps, cfg, sampler_name, scheduler, positive, negative, modelname, width, height, seed_value, loras = pipe

    def execute(self, pipe=None, steps=None, cfg=None, sampler_name=None, scheduler=None, positive=None, negative=None, modelname=None, width=None, height=None, seed_value=None, loras=None, vae_name=None):
        steps_original = None
        cfg_original = None
        sampler_name_original = None
        scheduler_original = None
        positive_original = None
        negative_original = None
        modelname_original = None
        width_original = None
        height_original = None
        seed_value_original = None
        loras_original = None
        vae_name_original = None

        if pipe != None:
            steps_original, cfg_original, sampler_name_original, scheduler_original, positive_original, negative_original, modelname_original, width_original, height_original, seed_value_original, loras_original, vae_name_original = pipe

        RBusAnyMod = []

        RBusAnyMod.append(steps if steps is not None else steps_original)
        RBusAnyMod.append(cfg if cfg is not None else cfg_original)
        RBusAnyMod.append(sampler_name if sampler_name is not None else sampler_name_original)
        RBusAnyMod.append(scheduler if scheduler is not None else scheduler_original)
        RBusAnyMod.append(positive if positive is not None else positive_original)
        RBusAnyMod.append(negative if negative is not None else negative_original)
        RBusAnyMod.append(modelname if modelname is not None else modelname_original)
        RBusAnyMod.append(width if width is not None else width_original)
        RBusAnyMod.append(height if height is not None else height_original)
        RBusAnyMod.append(seed_value if seed_value is not None else seed_value_original)
        RBusAnyMod.append(loras if loras is not None else loras_original)
        RBusAnyMod.append(vae_name if vae_name is not None else vae_name_original)


        return (RBusAnyMod,)

NODE_NAME = 'Pipe In Generation Data [RvTools]'
NODE_DESC = 'Pipe In Generation Data'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_In_Generation_Data
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
