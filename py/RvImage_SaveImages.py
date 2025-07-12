import os
import re
import comfy
import comfy.sd
import torch
import json
import numpy as np
import folder_paths
import hashlib

from PIL import Image
from PIL.PngImagePlugin import PngInfo
from typing import List

from ..core import CATEGORY, cstr

UPSCALE_MODELS = folder_paths.get_filename_list("upscale_models") + ["None"]
MAX_RESOLUTION = 32768

ALLOWED_EXT = ('.jpeg', '.jpg', '.png', '.tiff', '.gif', '.bmp', '.webp')

"""
Given the file path, finds a matching sha256 file, or creates one
based on the headers in the source file
"""
def get_sha256(file_path: str):
    file_no_ext = os.path.splitext(file_path)[0]
    hash_file = file_no_ext + ".sha256"

    if os.path.exists(hash_file):
        try:
            with open(hash_file, "r") as f:
                return f.read().strip()
        except OSError as e:
            cstr(f"RvTools: Error reading existing hash file: {e}").error.print()

    sha256_hash = hashlib.sha256()
    cstr(f"Hashing File (SHA256): {file_path}").msg.print()

    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    try:
        with open(hash_file, "w") as f:
            f.write(sha256_hash.hexdigest())
    except OSError as e:
        cstr(f"RvTools: Error writing hash to {hash_file}: {e}").error.print()

    return sha256_hash.hexdigest()

"""
Represent the given embedding name as key as detected by civitAI
"""
def civitai_embedding_key_name(embedding: str):
    return f'embed:{embedding}'
#---------------------------------------------------------------------------------------------------------------------#

"""
Represent the given lora name as key as detected by civitAI
NB: this should also work fine for Lycoris
"""
def civitai_lora_key_name(lora: str):
    return f'LORA:{lora}'
#---------------------------------------------------------------------------------------------------------------------#

def civitai_model_key_name(model: str):
    return f'Model:{model}'
#---------------------------------------------------------------------------------------------------------------------#

"""
Based on a embedding name, eg: EasyNegative, finds the path as known in comfy, including extension
"""
def full_embedding_path_for(embedding: str):
    matching_embedding = next((x for x in __list_embeddings() if x.startswith(embedding)), None)
    if matching_embedding == None:
        return None
    return folder_paths.get_full_path("embeddings", matching_embedding)
#---------------------------------------------------------------------------------------------------------------------#

"""
Based on a lora name, e.g., 'epi_noise_offset2', finds the path as known in comfy, including extension.
"""
def full_lora_path_for(lora: str):
    # Find the position of the last dot
    last_dot_position = lora.rfind('.')
    # Get the extension including the dot
    extension = lora[last_dot_position:] if last_dot_position != -1 else ""
    # Check if the extension is supported, if not, add .safetensors
    if extension not in folder_paths.supported_pt_extensions:
        lora += ".safetensors"

    # Find the matching lora path
    matching_lora = next((x for x in __list_loras() if x.endswith(lora)), None)
    if matching_lora is None:
        cstr(f'RvTools: could not find full path to lora "{lora}"').error.print()
        return None
    return folder_paths.get_full_path("loras", matching_lora)


def __list_loras():
    return folder_paths.get_filename_list("loras")

def __list_embeddings():
    return folder_paths.get_filename_list("embeddings")

#---------------------------------------------------------------------------------------------------------------------#

"""
Extracts Embeddings and Lora's from the given prompts
and allows asking for their sha's 
This module is based on civit's plugin and website implementations
The image saver node goes through the automatic flow, not comfy, on civit
see: https://github.com/civitai/sd_civitai_extension/blob/2008ba9126ddbb448f23267029b07e4610dffc15/scripts/gen_hashing.py
see: https://github.com/civitai/civitai/blob/d83262f401fb372c375e6222d8c2413fa221c2c5/src/utils/metadata/automatic.metadata
"""
class PromptMetadataExtractor:
    # Anything that follows embedding:<characters except , or whitespace
    EMBEDDING = r'embedding:([^,\s\(\)\:]+)'
    # Anything that follows <lora:NAME> with allowance for :weight, :weight.fractal or LBW
    LORA = r'<lora:([^>:]+)(?::[^>]+)?>'

    def __init__(self, prompts: List[str]):
        self.__embeddings = {}
        self.__loras = {}
        self.__perform(prompts)

    """
    Returns the embeddings used in the given prompts in a format as known by civitAI
    Example output: {"embed:EasyNegative": "66a7279a88", "embed:FastNegativeEmbedding": "687b669d82", "embed:ng_deepnegative_v1_75t": "54e7e4826d", "embed:imageSharpener": "fe5a4dfc4a"}
    """
    def get_embeddings(self):
        return self.__embeddings
        
    """
    Returns the lora's used in the given prompts in a format as known by civitAI
    Example output: {"LORA:epi_noiseoffset2": "81680c064e", "LORA:GoodHands-beta2": "ba43b0efee"}
    """
    def get_loras(self):
        return self.__loras

    # Private API
    def __perform(self, prompts):
        for prompt in prompts:
            embeddings = re.findall(self.EMBEDDING, prompt, re.IGNORECASE | re.MULTILINE)
            for embedding in embeddings:
                self.__extract_embedding_information(embedding)
            
            loras = re.findall(self.LORA, prompt, re.IGNORECASE | re.MULTILINE)
            for lora in loras:
                self.__extract_lora_information(lora)

    def __extract_embedding_information(self, embedding: str):
        embedding_name = civitai_embedding_key_name(embedding)
        embedding_path = full_embedding_path_for(embedding)
        if embedding_path == None:
            return
        sha = self.__get_shortened_sha(embedding_path)
        # Based on https://github.com/civitai/sd_civitai_extension/blob/2008ba9126ddbb448f23267029b07e4610dffc15/scripts/gen_hashing.py#L53
        self.__embeddings[embedding_name] = sha

    def __extract_lora_information(self, lora: str):
        lora_name = civitai_lora_key_name(lora)
        lora_path = full_lora_path_for(lora)
        if lora_path == None:
            return
        sha = self.__get_shortened_sha(lora_path)
        # Based on https://github.com/civitai/sd_civitai_extension/blob/2008ba9126ddbb448f23267029b07e4610dffc15/scripts/gen_hashing.py#L63
        self.__loras[lora_name] = sha
    
    def __get_shortened_sha(self, file_path: str):
       return get_sha256(file_path)[:10]


def return_filename(ckpt_name):
    return os.path.basename(ckpt_name)

#---------------------------------------------------------------------------------------------------------------------------------------------------#
def return_filename_without_extension(ckpt_name):
    return os.path.splitext(return_filename(ckpt_name))[0]

#---------------------------------------------------------------------------------------------------------------------------------------------------#
def handle_whitespace(string: str):
    return string.strip().replace("\n", " ").replace("\r", " ").replace("\t", " ")

#---------------------------------------------------------------------------------------------------------------------------------------------------##---------------------------------------------------------------------------------------------------------------------------------------------------#
def save_json(image_info, filename):
    try:
        workflow = (image_info or {}).get('workflow')
        if workflow is None:
            cstr(f"No image info found, skipping saving of JSON").warning.print()
        with open(f'{filename}.json', 'w') as workflow_file:
            json.dump(workflow, workflow_file)
            cstr(f"Workflow saved to: {filename + '.json'}").msg.print()
    except Exception as e:
        cstr(f'Failed to save workflow as json due to: {e}, proceeding with the remainder of saving execution').error.print()

#---------------------------------------------------------------------------------------------------------------------------------------------------#
#based on Was-node-suite & image saver
class RvImage_SaveImages:
    def __init__(self):
        self.output_dir = folder_paths.output_directory
        self.civitai_sampler_map = {
            'euler_ancestral': 'Euler a',
            'euler': 'Euler',
            'lms': 'LMS',
            'heun': 'Heun',
            'dpm_2': 'DPM2',
            'dpm_2_ancestral': 'DPM2 a',
            'dpmpp_2s_ancestral': 'DPM++ 2S a',
            'dpmpp_2m': 'DPM++ 2M',
            'dpmpp_sde': 'DPM++ SDE',
            'dpmpp_2m_sde': 'DPM++ 2M SDE',
            'dpmpp_3m_sde': 'DPM++ 3M SDE',
            'dpm_fast': 'DPM fast',
            'dpm_adaptive': 'DPM adaptive',
            'ddim': 'DDIM',
            'plms': 'PLMS',
            'uni_pc_bh2': 'UniPC',
            'uni_pc': 'UniPC',
            'lcm': 'LCM',
        }
        self.type = 'output'


    def get_civitai_sampler_name(self, sampler_name, scheduler):
        # based on: https://github.com/civitai/civitai/blob/main/src/server/common/constants.ts#L122
        if sampler_name in self.civitai_sampler_map:
            civitai_name = self.civitai_sampler_map[sampler_name]

            if scheduler == "karras":
                civitai_name += " Karras"
            elif scheduler == "exponential":
                civitai_name += " Exponential"
            elif scheduler == "sgm_uniform":
                civitai_name += " SGM Uniform"
            elif scheduler == "simple":
                civitai_name += " Simple"
            elif scheduler == "ddim_uniform":
                civitai_name += " DDIM Uniform"
            elif scheduler == "beta":
                civitai_name += " Beta"
            elif scheduler == "linear_quadratic":
                civitai_name += " Linear Quadratic"
            elif scheduler == "kl_optimal":
                civitai_name += " kl optimal"    
            elif scheduler == "AYS SDXL":
                civitai_name += " AYS SDXL"
            elif scheduler == "AYS SD1":
                civitai_name += " AYS SD1"
            elif scheduler == "AYS SVD":
                civitai_name += " AYS SVD"
            elif scheduler == "simple_test":
                civitai_name += " Simple Test"

            return civitai_name
        else:
            if scheduler != 'normal':
                return f"{sampler_name}_{scheduler}"
            else:
                return sampler_name

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE", ),
                "output_path": ("STRING", {"default": '[time(%Y-%m-%d)]', "multiline": False}),
                "filename_prefix": ("STRING", {"default": "image"}),
                "filename_delimiter": ("STRING", {"default":"_"}),
                "filename_number_padding": ("INT", {"default":4, "min":1, "max":9, "step":1}),
                "filename_number_start": ("BOOLEAN", {"default": False}),
                "extension": (['png', 'jpg', 'jpeg', 'gif', 'tiff', 'webp', 'bmp'], ),
                "dpi": ("INT", {"default": 300, "min": 1, "max": 2400, "step": 1}),
                "quality": ("INT", {"default": 100, "min": 1, "max": 100, "step": 1}),
                "optimize_image": ("BOOLEAN", {"default": False}),
                "lossless_webp": ("BOOLEAN", {"default": True}),
                "embed_workflow": ("BOOLEAN", {"default": True}),
                "save_generation_data": ("BOOLEAN", {"default": False}),
                "remove_prompts": ("BOOLEAN", {"default": False}),
                "save_workflow_as_json": ("BOOLEAN", {"default": False}),
                "pipe_v2": ("BOOLEAN", {"default": False}),
                "show_previews": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "pipe_opt": ("pipe",),
            },

            "hidden": {
                "prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.IMAGE.value
    
    RETURN_TYPES = ("IMAGE", "STRING",)
    RETURN_NAMES = ("images", "files",)

    FUNCTION = "save_images"

    OUTPUT_NODE = True

    def save_images(self, 
                        images, 
                        output_path='', 
                        filename_prefix="image", 
                        filename_delimiter='_', 
                        filename_number_padding=4, 
                        filename_number_start=False, 
                        extension='png', 
                        dpi=300, 
                        quality=100, 
                        optimize_image=False, 
                        lossless_webp=True, 
                        embed_workflow=True, 
                        save_generation_data=False,
                        remove_prompts=False,
                        save_workflow_as_json=False, 
                        show_previews=False, 
                        pipe_v2=False, 
                        pipe_opt=None,
                        prompt=None, 
                        extra_pnginfo=None
                        ):

        
        if pipe_opt != None:

            if pipe_v2:
                #GData II
                sampler_name, scheduler, steps, cfg, seed_value, width, height, positive, negative, modelname, vae_name, sloras = pipe_opt
            else:
                steps, cfg, sampler_name, scheduler, positive, negative, modelname, width, height, seed_value, sloras, vae_name = pipe_opt
  
            ckpt_path = ''
            diffusion_path = ''

            if positive in (None, '', 'undefined', 'none'): positive = ""
            if negative in (None, '', 'undefined', 'none'): negative = ""

            model_string = {}
            basemodelname = ''
            modelhash = ""

            if not modelname in (None, '', 'undefined', 'none') : 
                models = modelname.split(', ')

                for model in models:
                    if model != "":
                        ckpt_path = folder_paths.get_full_path("checkpoints", model)
                        diffusion_path = folder_paths.get_full_path("diffusion_models", model)
                        unet_path = folder_paths.get_full_path("unet", model)
                        upscaler_path = folder_paths.get_full_path("upscale_models", model)
        
                        if ckpt_path:
                            modelhash = get_sha256(ckpt_path)[:10]
                        elif diffusion_path:
                            modelhash = get_sha256(diffusion_path)[:10]
                        elif unet_path:
                            modelhash = get_sha256(unet_path)[:10]
                        elif upscaler_path:
                            modelhash = get_sha256(upscaler_path)[:10]
                    
                        if modelhash != "":
                            basemodelname = civitai_model_key_name(return_filename_without_extension(model))
                            model_string[basemodelname] = modelhash


            if not vae_name in (None, '', 'undefined', 'none') : 
                vae_full_path = folder_paths.get_full_path("vae", vae_name)
                vae_hash = get_sha256(vae_full_path)[:10]
                vae_file = return_filename_without_extension(vae_name)
                model_string[vae_file] = vae_hash

            xPositive = positive

            if not sloras in (None, '', 'undefined', 'none') : 
                xPositive += str(sloras) #add the loras temp. to the prompt for PromptMetadataExtractor

            metadata_extractor = PromptMetadataExtractor([xPositive, negative])
            embeddings = metadata_extractor.get_embeddings()
            loras = metadata_extractor.get_loras()

            if not sampler_name in (None, '', 'undefined', 'none') : 
               civitai_sampler_name = self.get_civitai_sampler_name(sampler_name.replace('_gpu', ''), scheduler)
            else:
                civitai_sampler_name = "Euler Simple"

            extension_hashes = json.dumps(model_string | embeddings | loras | { "model": modelhash })


            if not remove_prompts:
                positive_a111_params = handle_whitespace(positive) 
                negative_a111_params = f"\nNegative prompt: {handle_whitespace(negative)}"
                a111_params = f"{positive_a111_params}{negative_a111_params}\nSteps: {steps}, Sampler: {civitai_sampler_name}, CFG scale: {cfg}, Seed: {seed_value}, Size: {width}x{height}, Hashes: {extension_hashes}, Version: ComfyUI"
            else:
                positive_a111_params = ''
                negative_a111_params = f"\nNegative prompt: "
                a111_params = f"{positive_a111_params}{negative_a111_params}\nSteps: {steps}, Sampler: {civitai_sampler_name}, CFG scale: {cfg}, Seed: {seed_value}, Size: {width}x{height}, Hashes: {extension_hashes}, Version: ComfyUI"

        delimiter = filename_delimiter
        number_padding = filename_number_padding
        lossless_webp = (lossless_webp == True)
        optimize_image = (optimize_image == True)

        original_output = self.output_dir

        # Setup output path
        if output_path in [None, '', "none", "."]:
            output_path = self.output_dir

        if not os.path.isabs(output_path):
            output_path = os.path.join(self.output_dir, output_path)

        # Check output destination
        if output_path.strip() != '':
            if not os.path.isabs(output_path):
                output_path = os.path.join(folder_paths.output_directory, output_path)
            if not os.path.exists(output_path.strip()):
                cstr(f'The path `{output_path.strip()}` specified doesn\'t exist! Creating directory.').warning.print()
                os.makedirs(output_path, exist_ok=True)

        # Find existing counter values
        if filename_number_start:
            pattern = f"(\\d+){re.escape(delimiter)}{re.escape(filename_prefix)}"
        else:
            pattern = f"{re.escape(filename_prefix)}{re.escape(delimiter)}(\\d+)"
        existing_counters = [
            int(re.search(pattern, filename).group(1))
            for filename in os.listdir(output_path)
            if re.match(pattern, os.path.basename(filename))
        ]
        existing_counters.sort(reverse=True)

        # Set initial counter value
        if existing_counters:
            counter = existing_counters[0] + 1
        else:
            counter = 1


        # Set Extension
        file_extension = '.' + extension
        if file_extension not in ALLOWED_EXT:
            cstr(f"The extension `{extension}` is not valid. The valid formats are: {', '.join(sorted(ALLOWED_EXT))}").error.print()
            file_extension = ".png"

        results = list()
        output_files = list()
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            # Delegate metadata/pnginfo
            if extension == 'webp':
                img_exif = img.getexif()
                if embed_workflow:
                    workflow_metadata = ''
                    prompt_str = ''
                    if prompt is not None:
                        prompt_str = json.dumps(prompt)
                        img_exif[0x010f] = "Prompt:" + prompt_str
                    if extra_pnginfo is not None:
                        for x in extra_pnginfo:
                            workflow_metadata += json.dumps(extra_pnginfo[x])
                    img_exif[0x010e] = "Workflow:" + workflow_metadata
                exif_data = img_exif.tobytes()
            else:
                metadata = PngInfo()

                if embed_workflow:
                    if prompt is not None:
                        metadata.add_text("prompt", json.dumps(prompt))
                    if extra_pnginfo is not None:
                        for x in extra_pnginfo:
                            metadata.add_text(x, json.dumps(extra_pnginfo[x]))

                if pipe_opt != None and save_generation_data:
                    metadata.add_text("parameters", a111_params)

                exif_data = metadata

            # Delegate the filename stuffs
            if filename_number_start == True:
                file = f"{counter:0{number_padding}}{delimiter}{filename_prefix}{file_extension}"
                jsonfile = f"{counter:0{number_padding}}{delimiter}{filename_prefix}"
            else:
                file = f"{filename_prefix}{delimiter}{counter:0{number_padding}}{file_extension}"
                jsonfile = f"{filename_prefix}{delimiter}{counter:0{number_padding}}"
            if os.path.exists(os.path.join(output_path, file)):
                counter += 1

            # Save the images
            try:
                output_file = os.path.abspath(os.path.join(output_path, file))
                if extension in ["jpg", "jpeg"]:
                    img.save(output_file,
                             quality=quality, optimize=optimize_image, dpi=(dpi, dpi))
                elif extension == 'webp':
                    img.save(output_file,
                             quality=quality, lossless=lossless_webp, exif=exif_data)
                elif extension == 'png':
                    img.save(output_file,
                             pnginfo=exif_data, optimize=optimize_image)
                elif extension == 'bmp':
                    img.save(output_file)
                elif extension == 'tiff':
                    img.save(output_file,
                             quality=quality, optimize=optimize_image)
                else:
                    img.save(output_file,
                             pnginfo=exif_data, optimize=optimize_image)

                cstr(f"Image file saved to: {output_file}").msg.print()
                output_files.append(output_file)
                   
                if show_previews:
                    subfolder = self.get_subfolder_path(output_file, original_output)
                    results.append({
                        "filename": file,
                        "subfolder": subfolder,
                        "type": self.type
                    })

            except OSError as e:
                cstr(f'Unable to save file to: {output_file}').error.print()
                print(e)
            except Exception as e:
                cstr('Unable to save file due to the to the following error:').error.print()
                print(e)

            if save_workflow_as_json:
                output_json = os.path.abspath(os.path.join(output_path, jsonfile))
                save_json(extra_pnginfo, output_json)
                #output_files.append(jsonfile + ".json")

            counter += 1

        filtered_paths = []

        if filtered_paths:
            for image_path in filtered_paths:
                subfolder = self.get_subfolder_path(image_path, self.output_dir)
                image_data = {
                    "filename": os.path.basename(image_path),
                    "subfolder": subfolder,
                    "type": self.type
                }
                results.append(image_data)

        if show_previews == True:
            return {"ui": {"images": results, "files": output_files}, "result": (images, output_files,)}
        else:
            return {"ui": {"images": []}, "result": (images, output_files,)}

    def get_subfolder_path(self, image_path, output_path):
        output_parts = output_path.strip(os.sep).split(os.sep)
        image_parts = image_path.strip(os.sep).split(os.sep)
        common_parts = os.path.commonprefix([output_parts, image_parts])
        subfolder_parts = image_parts[len(common_parts):]
        subfolder_path = os.sep.join(subfolder_parts[:-1])
        return subfolder_path

NODE_NAME = 'Save Images [RvTools]'
NODE_DESC = 'Save Images'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvImage_SaveImages
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
