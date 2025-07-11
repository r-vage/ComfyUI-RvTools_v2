import comfy
import comfy.sd

from ..core import CATEGORY, cstr
from .anytype import AnyType

any = AnyType("*")

SAMPLERS_COMFY = comfy.samplers.KSampler.SAMPLERS
SCHEDULERS_ANY = comfy.samplers.KSampler.SCHEDULERS + ['AYS SD1', 'AYS SDXL', 'AYS SVD', 'GITS[coeff=1.2]','simple_test']

#code is taken from rgthree context utils
_all_context_input_output_data = {
  "base_ctx": ("base_ctx", "pipe", "context"),

  "model": ("model", "MODEL", "model"),
  "clip": ("clip", "CLIP", "clip"),
  "vae": ("vae", "VAE", "vae"),
  "positive": ("positive", "CONDITIONING", "positive"),
  "negative": ("negative", "CONDITIONING", "negative"),
  "cond_1": ("cond_1", "CONDITIONING", "cond_1"),
  "cond_2": ("cond_2", "CONDITIONING", "cond_2"),
  "cond_3": ("cond_3", "CONDITIONING", "cond_3"),
  "cond_4": ("cond_4", "CONDITIONING", "cond_4"),
  "latent": ("latent", "LATENT", "latent"),
  "images": ("images", "IMAGE", "images"),
  "image_ref": ("image_ref", "IMAGE", "image_ref"),
  "image_preproc": ("image_preproc", "IMAGE", "image_preproc"),
 
  "mask1": ("mask1", "MASK", "mask1"),
  "mask2": ("mask2", "MASK", "mask2"),
  "mask3": ("mask3", "MASK", "mask3"),
  "mask4": ("mask4", "MASK", "mask4"),

  "sampler": ("sampler", any, "sampler"),
  "sampler_d": ("sampler_d", any, "sampler_d"),
  
  "scheduler": ("scheduler", any, "scheduler"),
  "scheduler_d": ("scheduler_d", any, "scheduler_d"),

  "steps": ("steps", "INT", "steps"),
  "cfg": ("cfg", "FLOAT", "cfg"),
  "guidance": ("guidance", "FLOAT", "guidance"),
  "seed": ("seed", "INT", "seed"),
  
  "width": ("width", "INT", "width"),
  "height": ("height", "INT", "height"),
  "batch_size": ("batch_size", "INT", "batch_size"),
  "scale_by": ("scale_by", "FLOAT", "scale_by"),

  "text_pos": ("text_pos", "STRING", "text_pos"),
  "text_pos_i2p": ("text_pos_i2p", "STRING", "text_pos_i2p"),
  "text_neg": ("text_neg", "STRING", "text_neg"),
  "model_name": ("model_name", "STRING", "model_name"),
  "vae_name": ("vae_name", "STRING", "vae_name"),
  "lora_names": ("lora_names", "STRING", "lora_names"),

  "path": ("path", "STRING", "path"),
 }

force_input_types = ["INT", "STRING", "FLOAT"]
force_input_names = ["sampler", "scheduler"]

def _create_context_data(input_list=None):
  """Returns a tuple of context inputs, return types, and return names to use in a node"s def"""
  if input_list is None:
    input_list = _all_context_input_output_data.keys()
  
  list_ctx_return_types = []
  list_ctx_return_names = []
  ctx_optional_inputs = {}
  for inp in input_list:
    data = _all_context_input_output_data[inp]
    list_ctx_return_types.append(data[1])
    list_ctx_return_names.append(data[2])

    ctx_optional_inputs[data[0]] = tuple([data[1]] + ([{"forceInput": True}] if data[1] in force_input_types or data[0] in force_input_names else []))

  ctx_return_types = tuple(list_ctx_return_types)
  ctx_return_names = tuple(list_ctx_return_names)
  return (ctx_optional_inputs, ctx_return_types, ctx_return_names)


ALL_CTX_OPTIONAL_INPUTS, ALL_CTX_RETURN_TYPES, ALL_CTX_RETURN_NAMES = _create_context_data()


def new_context(base_ctx, **kwargs):
  """Creates a new context from the provided data, with an optional base ctx to start."""
  context = base_ctx if base_ctx is not None else None
  new_ctx = {}
  for key in _all_context_input_output_data:
    
    if key == "base_ctx":
      continue
    v = kwargs[key] if key in kwargs else None
    new_ctx[key] = v if v is not None else context[key] if context is not None and key in context else None
  return new_ctx

def get_context_return_tuple(ctx, inputs_list=None):
  """Returns a tuple for returning in the order of the inputs list."""
  if inputs_list is None:
    inputs_list = _all_context_input_output_data.keys()
  tup_list = [
    ctx,
  ]
  for key in inputs_list:
    if key == "base_ctx":
      continue
    tup_list.append(ctx[key] if ctx is not None and key in ctx else None)
  return tuple(tup_list)


class RvPipe_In_Context_iGEN_v3:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
          "required": {},
          "optional": ALL_CTX_OPTIONAL_INPUTS,
          "hidden": {},
        }

    RETURN_TYPES = ALL_CTX_RETURN_TYPES
    RETURN_NAMES = ALL_CTX_RETURN_NAMES

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.PIPE.value


    FUNCTION = "execute"

    def execute(self, base_ctx=None, **kwargs):  # pylint: disable = missing-function-docstring
      ctx = new_context(base_ctx, **kwargs)
      return get_context_return_tuple(ctx)

NODE_NAME = 'Pipe In Context iGEN v3 [RvTools]'
NODE_DESC = 'Pipe In Context iGEN v3'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_In_Context_iGEN_v3
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
