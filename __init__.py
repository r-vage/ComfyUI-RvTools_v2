import importlib.util
import os
import __main__

from .core import version, cstr

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

#! MESSAGE TEMPLATES
cstr.color.add_code("msg", f"{cstr.color.LIGHTGREEN}RvTools v2: {cstr.color.END}")
cstr.color.add_code("warning", f"{cstr.color.LIGHTGREEN}RvTools v2 {cstr.color.LIGHTYELLOW}Warning: {cstr.color.END}")
cstr.color.add_code("error", f"{cstr.color.RED}RvTools v2 {cstr.color.END}Error: {cstr.color.END}")

cstr(f'Version: {version}').msg.print()

def get_ext_dir(subpath=None, mkdir=False):
    dir = os.path.dirname(__file__)
    if subpath is not None:
        dir = os.path.join(dir, subpath)

    dir = os.path.abspath(dir)

    if mkdir and not os.path.exists(dir):
        os.makedirs(dir)
    return dir

py = get_ext_dir("py")
files = os.listdir(py)
for file in files:
    if not file.endswith(".py"):
        continue
    name = os.path.splitext(file)[0]
    imported_module = importlib.import_module(".py.{}".format(name), __name__)
    try:
        NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **imported_module.NODE_CLASS_MAPPINGS}
        NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **imported_module.NODE_DISPLAY_NAME_MAPPINGS}
    except:
        pass

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
#WEB_DIRECTORY = "./web"
