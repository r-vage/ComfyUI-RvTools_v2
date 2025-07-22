import os
import cv2
import numpy as np
import torch
from PIL import Image
import folder_paths

class WanVideoVaceSeamlessJoin:
    """
    Custom ComfyUI node for seamlessly joining video clips using WanVideo Vace encoder
    """
    
    def __init__(self):
        self.first_video_path = ""
        self.second_video_path = ""
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask_last_frames": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 1000,
                    "step": 1,
                    "display": "number"
                }),
                "mask_first_frames": ("INT", {
                    "default": 10,
                    "min": 0,
                    "max": 1000,
                    "step": 1,
                    "display": "number"
                }),
                "frame_load_cap": ("INT", {
                    "default": 81,
                    "min": 1,
                    "max": 10000,
                    "step": 1,
                    "display": "number"
                }),
            },
            "optional": {
                "first_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Full path to first video file - can be connected from other nodes"
                }),
                "second_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Full path to second video file - can be connected from other nodes"
                }),
            }
        }
    
    RETURN_TYPES = ("IMAGE", "IMAGE")
    RETURN_NAMES = ("image", "mask")
    FUNCTION = "process_videos"
    CATEGORY = "video/wanvideo"
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")  # Always execute to ensure fresh processing
    
    @classmethod
    def VALIDATE_INPUTS(cls, **kwargs):
        """Validate inputs before processing"""
        # Skip validation for optional inputs when they might be connected
        # Let the main processing function handle the validation
        return True
    
    def load_video_frames(self, video_path, max_frames=None):
        """Load video frames as numpy arrays"""
        if not os.path.exists(video_path):
            raise ValueError(f"Video file not found: {video_path}")
            
        cap = cv2.VideoCapture(video_path)
        
        # Check if video opened successfully
        if not cap.isOpened():
            cap.release()
            raise ValueError(f"Could not open video file: {video_path}")
        
        # Get video properties
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        print(f"[WanVideo] Video {video_path}: {total_frames} frames, {fps} fps")
        
        frames = []
        frame_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(frame_rgb)
            frame_count += 1
            
            if max_frames and frame_count >= max_frames:
                break
                
        cap.release()
        
        if not frames:
            raise ValueError(f"No frames could be loaded from video: {video_path}")
            
        print(f"[WanVideo] Successfully loaded {len(frames)} frames from {video_path}")
        return frames
    
    def create_solid_color_image(self, reference_frame, color_hex):
        """Create a solid color image with the same dimensions as reference frame"""
        height, width = reference_frame.shape[:2]
        
        # Convert hex color to RGB
        color_hex = color_hex.lstrip('#')
        r, g, b = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
        
        # Create solid color image
        solid_image = np.full((height, width, 3), [r, g, b], dtype=np.uint8)
        return solid_image
    
    def frames_to_tensor(self, frames_list):
        """Convert list of numpy frames to tensor format expected by ComfyUI"""
        if not frames_list:
            raise ValueError("Empty frames list provided")
            
        # Convert frames to tensor format (N, H, W, C) normalized to [0, 1]
        tensor_frames = []
        for frame in frames_list:
            # Normalize to [0, 1]
            normalized_frame = frame.astype(np.float32) / 255.0
            tensor_frames.append(normalized_frame)
        
        # Stack into tensor
        tensor_output = torch.from_numpy(np.stack(tensor_frames, axis=0))
        return tensor_output
    
    def process_videos(self, mask_last_frames, mask_first_frames, frame_load_cap, 
                      first_video_path=None, second_video_path=None):
        """Main processing function that joins the video clips"""
        
        print(f"[WanVideo] Starting process with parameters:")
        print(f"  mask_last_frames: {mask_last_frames}")
        print(f"  mask_first_frames: {mask_first_frames}")
        print(f"  frame_load_cap: {frame_load_cap}")
        print(f"  first_video_path: {first_video_path}")
        print(f"  second_video_path: {second_video_path}")
        
        # Handle None values (when inputs are not connected)
        if first_video_path is None:
            first_video_path = ""
        if second_video_path is None:
            second_video_path = ""
            
        # Convert to string and strip whitespace
        first_video_path = str(first_video_path).strip()
        second_video_path = str(second_video_path).strip()
        
        if not first_video_path or not second_video_path:
            raise ValueError("Both video files must be specified. Please provide full paths to both video files via connected string nodes or direct input.")
        
        # Check if files exist
        if not os.path.exists(first_video_path):
            raise ValueError(f"First video file not found: {first_video_path}")
        if not os.path.exists(second_video_path):
            raise ValueError(f"Second video file not found: {second_video_path}")
        
        print(f"[WanVideo] Both video files found, loading frames...")
        
        # Load video frames
        try:
            first_images_list = self.load_video_frames(first_video_path, frame_load_cap * 2)
            second_images_list = self.load_video_frames(second_video_path, frame_load_cap * 2)
            print(f"[WanVideo] Loaded {len(first_images_list)} frames from first video")
            print(f"[WanVideo] Loaded {len(second_images_list)} frames from second video")
        except Exception as e:
            print(f"[WanVideo] Error loading video frames: {str(e)}")
            raise ValueError(f"Error loading video frames: {str(e)}")
        
        if not first_images_list or not second_images_list:
            raise ValueError("Could not load frames from one or both videos")
        
        # Get reference frame for creating solid color images
        reference_frame = first_images_list[0]
        
        # 1. Creating output_images_list
        output_images_list = []
        
        # Calculate indices for first video
        first_images_start_index = frame_load_cap // 2
        first_images_end_index = frame_load_cap - mask_last_frames
        
        # Ensure indices are within bounds
        first_images_start_index = max(0, min(first_images_start_index, len(first_images_list)))
        first_images_end_index = max(first_images_start_index, min(first_images_end_index, len(first_images_list)))
        
        # Append first video frames
        for i in range(first_images_start_index, first_images_end_index):
            if i < len(first_images_list):
                output_images_list.append(first_images_list[i])
        
        # Calculate total mask count and add grey images
        total_mask_count = mask_last_frames + mask_first_frames
        grey_image = self.create_solid_color_image(reference_frame, "#7F7F7F")
        
        for _ in range(total_mask_count):
            output_images_list.append(grey_image.copy())
        
        # Calculate indices for second video
        second_images_start_index = mask_first_frames
        second_images_end_index = frame_load_cap // 2 
        
        # Ensure indices are within bounds
        second_images_start_index = max(0, min(second_images_start_index, len(second_images_list)))
        second_images_end_index = max(second_images_start_index, min(second_images_end_index, len(second_images_list)))
        
        # Append second video frames
        for i in range(second_images_start_index, second_images_end_index):
            if i < len(second_images_list):
                output_images_list.append(second_images_list[i])
        
        # 2. Creating output_mask_list
        output_mask_list = []
        
        # Calculate mask indices
        first_mask_start_index = frame_load_cap // 2
        first_mask_end_index = frame_load_cap - mask_last_frames 
        
        # Create black and white mask images
        black_image = self.create_solid_color_image(reference_frame, "#000000")
        white_image = self.create_solid_color_image(reference_frame, "#FFFFFF")
        
        # Add first section black masks
        first_mask_count = first_mask_end_index - first_mask_start_index
        first_mask_count = max(0, first_mask_count)
        
        for _ in range(first_mask_count):
            output_mask_list.append(black_image.copy())
        
        # Add white masks for transition area
        for _ in range(total_mask_count):
            output_mask_list.append(white_image.copy())
        
        # Add second section black masks
        second_mask_start_index = mask_first_frames
        second_mask_end_index = frame_load_cap // 2
        second_mask_count = second_mask_end_index - second_mask_start_index
        second_mask_count = max(0, second_mask_count)
        
        for _ in range(second_mask_count):
            output_mask_list.append(black_image.copy())
        
        # Convert to tensor format
        if not output_images_list:
            raise ValueError("No output images generated")
        if not output_mask_list:
            raise ValueError("No output masks generated")
        
        print(f"[WanVideo] Generated {len(output_images_list)} output images")
        print(f"[WanVideo] Generated {len(output_mask_list)} output masks")
        
        try:
            image_tensor = self.frames_to_tensor(output_images_list)
            mask_tensor = self.frames_to_tensor(output_mask_list)
            
            # Keep mask as RGB IMAGE type instead of converting to grayscale
            # This ensures compatibility with nodes expecting IMAGE input
            
            print(f"[WanVideo] Image tensor shape: {image_tensor.shape}")
            print(f"[WanVideo] Mask tensor shape: {mask_tensor.shape}")
            print(f"[WanVideo] Processing completed successfully")
            
            return (image_tensor, mask_tensor)
            
        except Exception as e:
            print(f"[WanVideo] Error creating tensors: {str(e)}")
            raise ValueError(f"Error creating output tensors: {str(e)}")

# ComfyUI Node Registration
NODE_CLASS_MAPPINGS = {
    "WanVideoVaceSeamlessJoin": WanVideoVaceSeamlessJoin
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WanVideoVaceSeamlessJoin": "WanVideo Vace Seamless Join"
}

# Note: For file upload functionality, users can now:
# 1. Connect string nodes (like "String Literal" or "Text" nodes) to the first_video_path and second_video_path inputs
# 2. Type the full path to their video files directly in the text fields when not connected
# 3. Use ComfyUI's input folder system by placing videos in the input directory
# 4. Create a custom web extension for file picker functionality