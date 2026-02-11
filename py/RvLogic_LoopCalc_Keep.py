import sys
import math
from typing import Tuple
import torch  # type: ignore

from ..core import CATEGORY, log

class RvLogic_LoopCalc_Keep:
    """Calculates frames to keep based on context length and total frames"""
    def __init__(self):
        pass
   
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "total_frames": ("INT", {"default": 16, "min": 1, "max": 10000, "step": 1}),
                "context_length": ("INT", {"default": 8, "min": 1, "max": 32, "step": 1}),
                "overlap_frames": ("INT", {"default": 4, "min": 0, "max": 32, "step": 1}),
                "image_loop_count": ("INT", {"default": 1, "min": 1, "max": 1000, "step": 1})
            }
        }

    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("frames_to_keep",)
    FUNCTION = "calculate"

    def calculate(self, total_frames: int, context_length: int, overlap_frames: int, image_loop_count: int) -> Tuple[int]:
        """
        Calculate frames to keep
        Returns:
            Tuple[int]: Single integer value in a tuple for frames to keep
        """
        try:
            # First calculation: effective stride
            effective_stride = context_length - overlap_frames

            # Second calculation: remaining frames
            remaining_frames = max(0, total_frames - image_loop_count)
            
            # Final calculation: minimum of both values
            frames_to_keep = min(effective_stride, remaining_frames)

            # Return as single-element tuple
            return (max(0, frames_to_keep),)

        except Exception as e:
            log.error("LoopCalcKeep", f"Frame calculation failed: {str(e)}")
            return (0,)

NODE_NAME = 'Keep Calculator [RvTools]'
NODE_DESC = 'Keep Calculator'

NODE_CLASS_MAPPINGS = {
    NODE_NAME: RvLogic_LoopCalc_Keep
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}