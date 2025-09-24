import json
import os
import random

from ..core import CATEGORY, cstr

class RvText_Prompt_Subject:
    JSON_FILE_PATH = 'subject.json'
    CATEGORY_KEYS = ['Character', 'Subject Type', 'Action', 'Action+', 'Action++', 'Positioning', 'Hair', 'Rare Hairstyle', 'Rare Hairstyle Man', 'Rare Hair Colors', 'Head Accessories', 'Face', 'Ears', 'Neck', 
                     'Skin', 'Clothing', 'Upper Body Decoration', 'Lower Body Decoration', 'Full body decoration', 'Shoes and socks', 'Accessories']
    
    def __init__(self):
        self.load_json()

    def load_json(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
        json_dir = os.path.join(parent_dir, 'json')
        json_file_path = os.path.join(json_dir, self.JSON_FILE_PATH)
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                self.options = json.load(f)
        except Exception as e:
            print(f"Error reading JSON file: {e}")  

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                **cls.get_input_types_from_keys(cls.CATEGORY_KEYS),
                "seed": ("INT", {"default": 0,"min": -1125899906842624,"max": 1125899906842624}),
            }
        }

    @staticmethod
    def get_input_types_from_keys(keys):
        input_types = {}
        for key in keys:
            input_types[key] = (tuple(RvText_Prompt_Subject.get_options_keys(key)), {"default": "None"})
        return input_types

    @staticmethod
    def get_options_keys(key):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
        json_dir = os.path.join(parent_dir, 'json')  
        json_file_path = os.path.join(json_dir, RvText_Prompt_Subject.JSON_FILE_PATH)
    
        with open(json_file_path, 'r', encoding='utf-8') as f:
            options = json.load(f)
            return list(options[key].keys())

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.TEXT.value

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "execute"

    def execute(self, **kwargs):
        prompt_parts = {}
        for key in self.CATEGORY_KEYS:
            if key in kwargs and kwargs[key] in self.options[key] and kwargs[key] != "None" and kwargs[key] != "Random":
                prompt_parts[key] = self.options[key][kwargs[key]]
        
            if key in kwargs and kwargs[key] in self.options[key] and kwargs[key] != "None" and kwargs[key] == "Random":
            #if kwargs.get("random") == "yes":
                Optional = list(self.options[key].keys())
                Optional.remove("None")
                Optional.remove("Random")
                Random_selection = random.choice(Optional)
                prompt_parts[key] = self.options[key][Random_selection]
        
        prompt_parts = {k: v for k, v in prompt_parts.items() if v}
        prompt = ','.join(prompt_parts.values()).strip()
        prompt += ','
        return (prompt,) if prompt else ('',)


NODE_NAME = 'Prompt Subject [RvTools]'
NODE_DESC = 'Prompt Subject'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvText_Prompt_Subject
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
