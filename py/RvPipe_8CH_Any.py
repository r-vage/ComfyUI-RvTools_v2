import comfy
import comfy.sd

from ..core import CATEGORY, cstr
from .anytype import AnyType

any = AnyType("*")


#code is taken from rgthree context utils
_all_context_input_output_data = {
  "pipe": ("pipe", "pipe", "pipe"),

  "any1": ("any1", any, "any1"),
  "any2": ("any2", any, "any2"),
  "any3": ("any3", any, "any3"),
  "any4": ("any4", any, "any4"),
  "any5": ("any5", any, "any5"),
  "any6": ("any6", any, "any6"),
  "any7": ("any7", any, "any7"),
  "any8": ("any8", any, "any8"),


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


def new_context(pipe, **kwargs):
  """Creates a new context from the provided data, with an optional base ctx to start."""
  context = pipe if pipe is not None else None
  new_ctx = {}
  for key in _all_context_input_output_data:
    
    if key == "pipe":
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
    if key == "pipe":
      continue
    tup_list.append(ctx[key] if ctx is not None and key in ctx else None)
  return tuple(tup_list)


class RvPipe_8CH_Any:
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

    def execute(self, pipe=None, **kwargs):  # pylint: disable = missing-function-docstring
      ctx = new_context(pipe, **kwargs)
      return get_context_return_tuple(ctx)

NODE_NAME = 'Pipe 8CH Any [RvTools]'
NODE_DESC = 'Pipe 8CH Any'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvPipe_8CH_Any
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
