import sys
import math
from typing import Tuple
import torch  # type: ignore

from ..core import CATEGORY, log

class RvLogic_LoopCalc:
    """Calculates required number of loops for processing frames with overlap"""
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "total_frames": ("INT", {"default": 16, "min": 1, "max": 10000, "step": 1}),
                "context_length": ("INT", {"default": 8, "min": 1, "max": 32, "step": 1}),
                "overlap_frames": ("INT", {"default": 4, "min": 0, "max": 32, "step": 1}),
                "images": ("IMAGE",)
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("total_loops",)
    
    FUNCTION = "calculate"

    def calculate(self, total_frames: int, context_length: int, overlap_frames: int, images) -> Tuple[int]:

        try:
            # Input validation
            if not isinstance(total_frames, int) or not isinstance(context_length, int) or not isinstance(overlap_frames, int):
                raise ValueError("Input parameters must be integers")

            # Get current number of frames from image input
            if isinstance(images, torch.Tensor):
                image_count = int(images.shape[0])  # Ensure integer
            else:
                image_count = 0
                
            # Calculate remaining frames needed
            remaining_frames = max(0, total_frames - image_count)
            
            # Calculate effective stride (minimum 1)
            effective_stride = max(1, context_length - overlap_frames)
            
            # Calculate loops needed
            if remaining_frames > 0:
                total_loops = math.ceil(remaining_frames / effective_stride)
            else:
                total_loops = 0  # No additional frames needed
                
            # Always return at least 1 loop, ensure integer
            result = max(1, int(total_loops))
            return (result,)

        except Exception as e:
            log.error("LoopCalc", f"Loop calculation failed: {str(e)}")
            return (1,)  # Return safe default as integer

NODE_NAME = 'Loop Calculator [RvTools]'
NODE_DESC = 'Loop Calculator'

NODE_CLASS_MAPPINGS = {
    NODE_NAME: RvLogic_LoopCalc
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}