import comfy
import comfy.sd

from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

#code is taken from rgthree context utils
_all_context_input_output_data = {
  "base_ctx": ("base_ctx", "pipe", "context"),

  "model": ("model", "MODEL", "model"),
  "clip": ("clip", "CLIP", "clip"),
  "vae": ("vae", "VAE", "vae"),
  "positive": ("positive", "CONDITIONING", "positive"),
  "negative": ("negative", "CONDITIONING", "negative"),
  "latent": ("latent", "LATENT", "latent"),

  "width": ("width", "INT", "width"),
  "height": ("height", "INT", "height"),

  "frame_rate": ("frame_rate", "FLOAT", "frame_rate"),
  "frame_load_cap": ("frame_load_cap", "INT", "frame_load_cap"),
  "skip_first_frames": ("skip_first_frames", "INT", "skip_first_frames"),
  "select_every_nth": ("select_every_nth", "INT", "select_every_nth"),
  
  "images_input": ("images_input", "IMAGE", "images_input"),
  "images_ref_start": ("images_ref_start", "IMAGE", "images_ref_start"),
  "images_ref_end": ("images_ref_end", "IMAGE", "images_ref_end"),
  "images_output": ("images_output", "IMAGE", "images_output"),

  "audio_input": ("audio_input", "AUDIO", "audio_input"),
  "audio_output": ("audio_output", "AUDIO", "audio_output"),

  "mask_1": ("mask_1", "MASK", "mask_1"),
  "mask_2": ("mask_2", "MASK", "mask_2"),
  
  "images_pp_1": ("images_pp_1", "IMAGE", "images_pp_1"),
  "images_pp_2": ("images_pp_2", "IMAGE", "images_pp_2"),
  "images_pp_3": ("images_pp_3", "IMAGE", "images_pp_3"),
  "images_pp_4": ("images_pp_4", "IMAGE", "images_pp_4"),
  "images_pp_5": ("images_pp_5", "IMAGE", "images_pp_5"),

  "any_1": ("any_1", any, "any_1"),
  "any_2": ("any_2", any, "any_2"),
  "any_3": ("any_3", any, "any_3"),
  "any_4": ("any_4", any, "any_4"),
  "any_5": ("any_5", any, "any_5"),

  "steps": ("steps", "INT", "steps"),
  "cfg": ("cfg", "FLOAT", "cfg"),
  "seed": ("seed", "INT", "seed"),

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
    ctx_optional_inputs[data[0]] = tuple([data[1]] + ([{
      "forceInput": True
    }] if data[1] in force_input_types or data[0] in force_input_names else []))

  ctx_return_types = tuple(list_ctx_return_types)
  ctx_return_names = tuple(list_ctx_return_names)
  return (ctx_optional_inputs, ctx_return_types, ctx_return_names)


ALL_CTX_OPTIONAL_INPUTS, ALL_CTX_RETURN_TYPES, ALL_CTX_RETURN_NAMES = _create_context_data()

_original_ctx_inputs_list = [
  "base_ctx", "model", "clip", "vae"
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


class RvPipe_In_Context_Video_v3:
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

NODE_NAME = 'Pipe In Context Video v3 [RvTools]'
NODE_DESC = 'Pipe In Context Video v3'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_In_Context_Video_v3
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
