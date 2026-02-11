# Common utility functions for RvTools_v2
# Centralized to avoid duplication across node files

import torch # type: ignore
import numpy as np # type: ignore
from datetime import datetime
from PIL import Image


# ============================================================================
# Date/Time Formatting Utilities
# ============================================================================

def format_datetime(datetime_format):
    """
    Format current datetime using specified format string
    
    Args:
        datetime_format: strftime format string
        
    Returns:
        Formatted datetime string, defaults to "%Y-%m-%d-%H%M%S" on error
    """
    today = datetime.now()
    try:
        timestamp = today.strftime(datetime_format)
    except:
        timestamp = today.strftime("%Y-%m-%d-%H%M%S")
    return timestamp


def format_date_time(string, position, datetime_format):
    """
    Add datetime to string as prefix or postfix
    
    Args:
        string: Base string
        position: "prefix" or "postfix"
        datetime_format: strftime format string
        
    Returns:
        String with datetime added
    """
    today = datetime.now()
    if position == "prefix":
        return f"{today.strftime(datetime_format)}_{string}"
    if position == "postfix":
        return f"{string}_{today.strftime(datetime_format)}"
    return string


def format_variables(string, input_variables):
    """
    Format string with comma-separated variables
    
    Args:
        string: Format string with {} placeholders
        input_variables: Comma-separated variable values
        
    Returns:
        Formatted string with variables inserted
    """
    if input_variables:
        variables = str(input_variables).split(",")
        return string.format(*variables)
    else:
        return string


# ============================================================================
# Image Conversion Utilities
# ============================================================================

def tensor2pil(image):
    """
    Convert torch tensor to PIL Image
    
    Args:
        image: Torch tensor [C, H, W] or [B, H, W, C]
        
    Returns:
        PIL Image
    """
    return Image.fromarray(
        np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)
    )


def pil2tensor(image):
    """
    Convert PIL Image to torch tensor
    
    Args:
        image: PIL Image
        
    Returns:
        Torch tensor [1, H, W, C] in range [0, 1]
    """
    return torch.from_numpy(
        np.array(image).astype(np.float32) / 255.0
    ).unsqueeze(0)


# ============================================================================
# Tensor Manipulation Utilities  
# ============================================================================

def permute_channels_first(image):
    """
    Permute tensor from [B, H, W, C] to [B, C, H, W]
    
    Args:
        image: Tensor in [B, H, W, C] format
        
    Returns:
        Tensor in [B, C, H, W] format
    """
    return image.permute([0, 3, 1, 2])


def permute_channels_last(image):
    """
    Permute tensor from [B, C, H, W] to [B, H, W, C]
    
    Args:
        image: Tensor in [B, C, H, W] format
        
    Returns:
        Tensor in [B, H, W, C] format
    """
    return image.permute([0, 2, 3, 1])


# Shorter aliases for convenience
p = permute_channels_first
pb = permute_channels_last


# ============================================================================
# Mask Utilities
# ============================================================================

def make_3d_mask(mask):
    """
    Ensure mask is 3D [B, H, W] format
    
    Args:
        mask: Torch tensor of shape [B, 1, H, W], [B, H, W], or [H, W]
        
    Returns:
        Torch tensor of shape [B, H, W]
    """
    if len(mask.shape) == 4:
        return mask.squeeze(0)
    elif len(mask.shape) == 2:
        return mask.unsqueeze(0)
    return mask
