from ..core import CATEGORY
from .anytype import AnyType

any = AnyType("*")

#from kjnodes
class RvText_WidgetToString:
#    @classmethod
#    def IS_CHANGED(cls, **kwargs):
#        return float("NaN")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "id": ("INT", {"default": 0, "min": 0, "max": 100000, "step": 1}),
                "widget_name": ("STRING", {"multiline": False}),
                "return_all": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                         "any_input": (any, {}),
                         "node_title": ("STRING", {"multiline": False}),
                         "allowed_float_decimals": ("INT", {"default": 2, "min": 0, "max": 10, "tooltip": "Number of decimal places to display for float values"}),
                         
                         },
            "hidden": {"extra_pnginfo": "EXTRA_PNGINFO",
                       "prompt": "PROMPT",
                       "unique_id": "UNIQUE_ID",},
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.TEXT.value
    RETURN_TYPES = ("STRING", )
    
    FUNCTION = "execute"

    def execute(self, id, widget_name, extra_pnginfo, prompt, unique_id, return_all=False, any_input=None, node_title="", allowed_float_decimals=2):
        workflow = extra_pnginfo["workflow"]
        #print(json.dumps(workflow, indent=4))
        results = []
        node_id = None  # Initialize node_id to handle cases where no match is found
        link_id = None
        link_to_node_map = {}

        for node in workflow["nodes"]:
            if node_title:
                if "title" in node:
                    if node["title"] == node_title:
                        node_id = node["id"]
                        break
                else:
                    print("Node title not found.")
            elif id != 0:
                if node["id"] == id:
                    node_id = id
                    break
            elif any_input is not None:
                if node["type"] == "Widget to String [RvTools]" and node["id"] == int(unique_id) and not link_id:
                    for node_input in node["inputs"]:
                        if node_input["name"] == "any_input":
                            link_id = node_input["link"]
                    
                # Construct a map of links to node IDs for future reference
                node_outputs = node.get("outputs", None)
                if not node_outputs:
                    continue
                for output in node_outputs:
                    node_links = output.get("links", None)
                    if not node_links:
                        continue
                    for link in node_links:
                        link_to_node_map[link] = node["id"]
                        if link_id and link == link_id:
                            break
        
        if link_id:
            node_id = link_to_node_map.get(link_id, None)

        if node_id is None:
            raise ValueError("No matching node found for the given title or id")

        values = prompt[str(node_id)]
        if "inputs" in values:
            if return_all:
                # Format items based on type
                formatted_items = []
                for k, v in values["inputs"].items():
                    if isinstance(v, float):
                        item = f"{k}: {v:.{allowed_float_decimals}f}"
                    else:
                        item = f"{k}: {str(v)}"
                    formatted_items.append(item)
                results.append(', '.join(formatted_items))
            elif widget_name in values["inputs"]:
                v = values["inputs"][widget_name]
                if isinstance(v, float):
                    v = f"{v:.{allowed_float_decimals}f}"
                else:
                    v = str(v)
                return (v, )
            else:
                raise NameError(f"Widget not found: {node_id}.{widget_name}")
        return (', '.join(results).strip(', '), )

NODE_NAME = 'Widget to String [RvTools]'
NODE_DESC = 'Widget to String'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvText_WidgetToString
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}