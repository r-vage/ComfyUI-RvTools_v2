import comfy
import comfy.sd

from .anytype import *
from ..core import CATEGORY

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
  "latent": ("latent", "LATENT", "latent"),
  "images": ("images", "IMAGE", "images"),
  "images_ref": ("images_ref", "IMAGE", "images_ref"),

  "images_cn1": ("images_cn1", "IMAGE", "images_cn1"),
  "images_cn2": ("images_cn2", "IMAGE", "images_cn2"),
  "images_cn3": ("images_cn3", "IMAGE", "images_cn3"),
  "images_cn4": ("images_cn4", "IMAGE", "images_cn4"),
  "images_cn5": ("images_cn5", "IMAGE", "images_cn5"),
 
  "mask1": ("mask1", "MASK", "mask1"),
  "mask2": ("mask2", "MASK", "mask2"),
  "mask3": ("mask3", "MASK", "mask3"),
  "mask4": ("mask4", "MASK", "mask4"),
  "mask5": ("mask5", "MASK", "mask5"),

  "audio": ("audio", "AUDIO", "audio"),

  "sampler": ("sampler", any, "sampler"),
  "scheduler": ("scheduler", any, "scheduler"),
  
  "steps": ("steps", "INT", "steps"),
  "cfg": ("cfg", "FLOAT", "cfg"),
  "seed": ("seed", "INT", "seed"),

  "frame_rate": ("frame_rate", "FLOAT", "frame_rate"),

  "width": ("width", "INT", "width"),
  "height": ("height", "INT", "height"),

  "load_cap": ("load_cap", "INT", "load_cap"),
  "batch_size": ("batch_size", "INT", "batch_size"),
  "skip_first_frames": ("skip_first_frames", "INT", "skip_first_frames"),
  "select_every_nth": ("select_every_nth", "INT", "select_every_nth"),

  "img_in_prev": ("img_in_prev", "INT", "img_in_prev"),
  "img_in_filter_prev": ("img_in_filter_prev", "INT", "imgs_in_filter_prev"),
  "prev_crop_pos": ("prev_crop_pos", ["center","top", "bottom", "left", "right"], "prev_crop_pos"),
  "prev_crop_interpol": ("prev_crop_interpol", ["lanczos", "nearest", "bilinear", "bicubic", "area", "nearest-exact"], "prev_crop_interpol"),

  "scale_by": ("scale_by", "FLOAT", "scale_by"),
  "images_per_batch": ("images_per_batch", "INT", "images_per_batch"),

  "text_pos": ("text_pos", "STRING", "text_pos"),
  "text_neg": ("text_neg", "STRING", "text_neg"),

  "path": ("path", "STRING", "path"),
 }

force_input_types = ["INT", "STRING", "FLOAT"]
force_input_names = ["sampler", "scheduler", "prev_crop_pos", "prev_crop_interpol"]

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
    ctx_optional_inputs[data[0]] = tuple([data[1]] + ([{
      "forceInput": True
    }] if data[1] in force_input_types or data[0] in force_input_names else []))

  ctx_return_types = tuple(list_ctx_return_types)
  ctx_return_names = tuple(list_ctx_return_names)
  return (ctx_optional_inputs, ctx_return_types, ctx_return_names)


ALL_CTX_OPTIONAL_INPUTS, ALL_CTX_RETURN_TYPES, ALL_CTX_RETURN_NAMES = _create_context_data()

_original_ctx_inputs_list = [
  "base_ctx", "model", "clip", "vae", "positive", "negative", "latent", "images", "seed"
]
ORIG_CTX_OPTIONAL_INPUTS, ORIG_CTX_RETURN_TYPES, ORIG_CTX_RETURN_NAMES = _create_context_data(
  _original_ctx_inputs_list)


def new_context(base_ctx, **kwargs):
  """Creates a new context from the provided data, with an optional base ctx to start."""
  context = base_ctx if base_ctx is not None else None
  new_ctx = {}
  for key in _all_context_input_output_data:
    if key == "base_ctx":
      continue
    v = kwargs[key] if key in kwargs else None
    new_ctx[key] = v if v is not None else context[
      key] if context is not None and key in context else None
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


class RvPipe_In_Context_vGEN_v2:
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

NODE_NAME = 'Pipe In Context vGEN v2 [RvTools]'
NODE_DESC = 'Pipe In Context vGEN v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_In_Context_vGEN_v2
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
