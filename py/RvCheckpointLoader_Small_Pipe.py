import comfy
import comfy.sd
import torch
import folder_paths
from typing import List, Tuple, Optional, Union, Any
from pathlib import Path

from ..core import CATEGORY, cstr

MAX_RESOLUTION: int = 32768

class RvCheckpointLoader_Small_Pipe:
    """Checkpoint loader with improved type safety and error handling"""
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"),),
                "vae_name": (["Baked VAE"] + folder_paths.get_filename_list("vae"),),
                "Baked_Clip": ("BOOLEAN", {"default": True},),
                "Use_Clip_Layer": ("BOOLEAN", {"default": True},),
                "stop_at_clip_layer": ("INT", {"default": -2, "min": -24, "max": -1, "step": 1},),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
            },
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.DEPRECATED.value
    RETURN_TYPES = ("pipe",)
    FUNCTION = "execute"
    DEPRECATED = True

    def execute(self, 
                ckpt_name: str, 
                vae_name: str, 
                Baked_Clip: bool, 
                Use_Clip_Layer: bool, 
                stop_at_clip_layer: int, 
                batch_size: int) -> Tuple[List[Any]]:
        """
        Execute checkpoint loading with improved error handling
        
        Args:
            ckpt_name: Name of checkpoint file
            vae_name: Name of VAE file or "Baked VAE"
            Baked_Clip: Whether to use baked CLIP
            Use_Clip_Layer: Whether to use CLIP layer stopping
            stop_at_clip_layer: CLIP layer to stop at
            batch_size: Batch size for processing
            
        Returns:
            Tuple containing pipe list with loaded components
        """
        try:
            # Validate inputs
            if not ckpt_name:
                raise ValueError("Checkpoint name cannot be empty")
            
            if batch_size <= 0:
                raise ValueError("Batch size must be positive")
                
            # Get checkpoint path
            ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
            if not ckpt_path or not Path(ckpt_path).exists():
                raise FileNotFoundError(f"Checkpoint not found: {ckpt_name}")

            # Load checkpoint
            output_vae = (vae_name == "Baked VAE")
            loaded_ckpt = comfy.sd.load_checkpoint_guess_config(
                ckpt_path, 
                output_vae=output_vae, 
                output_clip=Baked_Clip, 
                embedding_directory=folder_paths.get_folder_paths("embeddings")
            )

            # Load VAE
            loaded_vae = self._load_vae(vae_name, loaded_ckpt)
            
            # Load CLIP
            loaded_clip = self._load_clip(Baked_Clip, Use_Clip_Layer, stop_at_clip_layer, loaded_ckpt)

            # Build result list with proper types
            return (self._build_pipe_result(
                loaded_ckpt, loaded_clip, loaded_vae, 
                batch_size, ckpt_name, vae_name
            ),)

        except Exception as e:
            cstr(f"Checkpoint loading failed: {str(e)}").error.print()
            # Return safe defaults
            return (self._get_default_pipe(),)

    def _load_vae(self, vae_name: str, loaded_ckpt: Any) -> Any:
        """Load VAE with error handling"""
        try:
            if vae_name == "Baked VAE":
                return loaded_ckpt[:3][2]
            else:
                vae_path = folder_paths.get_full_path("vae", vae_name)
                if not vae_path or not Path(vae_path).exists():
                    raise FileNotFoundError(f"VAE not found: {vae_name}")
                return comfy.sd.VAE(sd=comfy.utils.load_torch_file(vae_path))
        except Exception as e:
            cstr(f"VAE loading failed: {str(e)}").error.print()
            return None

    def _load_clip(self, Baked_Clip: bool, Use_Clip_Layer: bool, 
                   stop_at_clip_layer: int, loaded_ckpt: Any) -> Optional[Any]:
        """Load CLIP with error handling"""
        try:
            if Baked_Clip:
                loaded_clip = loaded_ckpt[:3][1].clone()
                if Use_Clip_Layer:
                    loaded_clip.clip_layer(stop_at_clip_layer)
                return loaded_clip
            return None
        except Exception as e:
            cstr(f"CLIP loading failed: {str(e)}").error.print()
            return None

    def _build_pipe_result(self, loaded_ckpt: Any, loaded_clip: Optional[Any], 
                          loaded_vae: Any, batch_size: int, 
                          ckpt_name: str, vae_name: str) -> List[Any]:
        """Build pipe result list with proper types"""
        return [
            loaded_ckpt[:3][0],         # model
            loaded_clip,                # clip
            loaded_vae,                 # vae
            None,                       # latent
            8,                          # width (int)
            8,                          # height (int)
            max(1, int(batch_size)),    # batch_size (validated)
            str(ckpt_name),             # model_name
            "" if vae_name == "Baked VAE" else str(vae_name)  # vae_name
        ]

    def _get_default_pipe(self) -> List[Any]:
        """Return safe default pipe values"""
        return [
            None,   # model
            None,   # clip
            None,   # vae
            None,   # latent
            8,      # width
            8,      # height
            1,      # batch_size
            "",     # model_name
            ""      # vae_name
        ]


NODE_NAME = 'Checkpoint Loader Small (Pipe) [RvTools]'
NODE_DESC = 'Checkpoint Loader Small (Pipe)'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvCheckpointLoader_Small_Pipe
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
