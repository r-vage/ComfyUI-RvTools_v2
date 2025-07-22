import os
import cv2
import numpy as np
import torch
from PIL import Image

class CombineVideoClips:
    """
    Custom ComfyUI node for combining multiple video clips
    """
    
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "frame_load_cap": ("INT", {
                    "default": 81,
                    "min": 1,
                    "max": 10000,
                    "step": 1,
                    "display": "number",
                    "tooltip": "Total number of frames to load from each video"
                }),
                "mask_last_frames": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 1000,
                    "step": 1,
                    "display": "number",
                    "tooltip": "Number of last frames to mask in the first video"
                }),
                "mask_first_frames": ("INT", {
                    "default": 10,
                    "min": 0,
                    "max": 1000,
                    "step": 1,
                    "display": "number",
                    "tooltip": "Number of first frames to mask in the last video"
                }),
            },
            "optional": {
                "first_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Path to the first video file - can be connected from other nodes"
                }),
                "first_joined_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Path to the first joined video file (optional) - can be connected from other nodes"
                }),
                "second_joined_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Path to the second joined video file (optional) - can be connected from other nodes"
                }),
                "third_joined_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Path to the third joined video file (optional) - can be connected from other nodes"
                }),
                "fourth_joined_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Path to the fourth joined video file (optional) - can be connected from other nodes"
                }),
                "fifth_joined_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Path to the fifth joined video file (optional) - can be connected from other nodes"
                }),                   
                "last_video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                    "tooltip": "Path to the last video file - can be connected from other nodes"
                }),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "combine_videos"
    CATEGORY = "video/combine"
    
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
        print(f"[CombineVideo] Video {video_path}: {total_frames} frames, {fps} fps")
        
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
            
        print(f"[CombineVideo] Successfully loaded {len(frames)} frames from {video_path}")
        return frames
    
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
    
    def combine_videos(self, frame_load_cap, mask_last_frames, mask_first_frames,
                      first_video_path=None, first_joined_video_path=None, second_joined_video_path=None,
                      third_joined_video_path=None, fourth_joined_video_path=None, fifth_joined_video_path=None, 
                      last_video_path=None):
        """Main processing function that combines the video clips"""
        
        print(f"[CombineVideo] Starting combine process with parameters:")
        print(f"  frame_load_cap: {frame_load_cap}")
        print(f"  mask_last_frames: {mask_last_frames}")
        print(f"  mask_first_frames: {mask_first_frames}")
        print(f"  first_video_path: {first_video_path}")
        print(f"  first_joined_video_path: {first_joined_video_path}")
        print(f"  second_joined_video_path: {second_joined_video_path}")
        print(f"  third_joined_video_path: {third_joined_video_path}")
        print(f"  fourth_joined_video_path: {fourth_joined_video_path}")
        print(f"  fifth_joined_video_path: {fifth_joined_video_path}")        
        print(f"  last_video_path: {last_video_path}")
        
        # Handle None values (when inputs are not connected)
        if first_video_path is None:
            first_video_path = ""
        if first_joined_video_path is None:
            first_joined_video_path = ""
        if second_joined_video_path is None:
            second_joined_video_path = ""
        if third_joined_video_path is None:
            third_joined_video_path = ""
        if fourth_joined_video_path is None:
            fourth_joined_video_path = ""
        if fifth_joined_video_path is None:
            fifth_joined_video_path = ""
        if last_video_path is None:
            last_video_path = ""
        
        # Convert to string and clean up paths
        first_video_path = str(first_video_path).strip()
        first_joined_video_path = str(first_joined_video_path).strip()
        second_joined_video_path = str(second_joined_video_path).strip()
        third_joined_video_path = str(third_joined_video_path).strip()
        fourth_joined_video_path = str(fourth_joined_video_path).strip()
        fifth_joined_video_path = str(fifth_joined_video_path).strip()
        last_video_path = str(last_video_path).strip()
        
        # Validate required paths
        if not first_video_path or not last_video_path:
            raise ValueError("First video path and last video path are required. Please provide full paths via connected string nodes or direct input.")
        
        # Check if required files exist
        if not os.path.exists(first_video_path):
            raise ValueError(f"First video file not found: {first_video_path}")
        if not os.path.exists(last_video_path):
            raise ValueError(f"Last video file not found: {last_video_path}")
        
        print(f"[CombineVideo] Loading video frames...")
        
        # Load video frames from all provided videos
        try:
            # Load first video (required)
            first_images_list = self.load_video_frames(first_video_path, frame_load_cap)
            
            # Load joined videos (optional)
            first_joined_images_list = []
            if first_joined_video_path and os.path.exists(first_joined_video_path):
                first_joined_images_list = self.load_video_frames(first_joined_video_path)
                
            second_joined_images_list = []
            if second_joined_video_path and os.path.exists(second_joined_video_path):
                second_joined_images_list = self.load_video_frames(second_joined_video_path)
                
            third_joined_images_list = []
            if third_joined_video_path and os.path.exists(third_joined_video_path):
                third_joined_images_list = self.load_video_frames(third_joined_video_path)

            fourth_joined_images_list = []
            if fourth_joined_video_path and os.path.exists(fourth_joined_video_path):
                fourth_joined_images_list = self.load_video_frames(fourth_joined_video_path)
 
            fifth_joined_images_list = []
            if fifth_joined_video_path and os.path.exists(fifth_joined_video_path):
                fifth_joined_images_list = self.load_video_frames(fifth_joined_video_path)
  
            # Load final video (required)
            final_images_list = self.load_video_frames(last_video_path, frame_load_cap)
            
            print(f"[CombineVideo] Loaded frames:")
            print(f"  First video: {len(first_images_list)} frames")
            print(f"  First joined: {len(first_joined_images_list)} frames")
            print(f"  Second joined: {len(second_joined_images_list)} frames")
            print(f"  Third joined: {len(third_joined_images_list)} frames")
            print(f"  Fourth joined: {len(fourth_joined_images_list)} frames")
            print(f"  Fifth joined: {len(fifth_joined_images_list)} frames")            
            print(f"  Final video: {len(final_images_list)} frames")
            
        except Exception as e:
            print(f"[CombineVideo] Error loading video frames: {str(e)}")
            raise ValueError(f"Error loading video frames: {str(e)}")
        
        # 1. Creating output_images_list
        output_images_list = []
        
        # a-f: Create all image lists (already done above)
        
        # g: Store 0 in first_images_start_index
        first_images_start_index = 0
        
        # h: Calculate frame_load_cap // 2 and store in first_images_end_index
        first_images_end_index = frame_load_cap // 2
        
        # Ensure indices are within bounds
        first_images_end_index = min(first_images_end_index, len(first_images_list))
        
        # i: Append images from first_images_list to output_images_list
        print(f"[CombineVideo] Adding first video frames [{first_images_start_index}:{first_images_end_index}]")
        for i in range(first_images_start_index, first_images_end_index):
            if i < len(first_images_list):
                output_images_list.append(first_images_list[i])
        
        # j: If first_joined_images_list is not empty, append all its images
        if first_joined_images_list:
            print(f"[CombineVideo] Adding first joined video frames: {len(first_joined_images_list)}")
            output_images_list.extend(first_joined_images_list)
        
        # k: If second_joined_images_list is not empty, append all its images
        if second_joined_images_list:
            print(f"[CombineVideo] Adding second joined video frames: {len(second_joined_images_list)}")
            output_images_list.extend(second_joined_images_list)
        
        # l: If third_joined_images_list is not empty, append all its images
        if third_joined_images_list:
            print(f"[CombineVideo] Adding third joined video frames: {len(third_joined_images_list)}")
            output_images_list.extend(third_joined_images_list)
        
        # m: If fourth_joined_images_list is not empty, append all its images
        if fourth_joined_images_list:
            print(f"[CombineVideo] Adding fourth joined video frames: {len(fourth_joined_images_list)}")
            output_images_list.extend(fourth_joined_images_list)

        # n: If fifth_joined_images_list is not empty, append all its images
        if fifth_joined_images_list:
            print(f"[CombineVideo] Adding fifth joined video frames: {len(fifth_joined_images_list)}")
            output_images_list.extend(fifth_joined_images_list)

        # o: Calculate frame_load_cap // 2 and store in final_images_start_index
        final_images_start_index = frame_load_cap // 2
        
        # Ensure start index is within bounds
        final_images_start_index = min(final_images_start_index, len(final_images_list))
        
        # p: Append images from final_images_list starting from final_images_start_index to end
        print(f"[CombineVideo] Adding final video frames [{final_images_start_index}:{len(final_images_list)}]")
        for i in range(final_images_start_index, len(final_images_list)):
            output_images_list.append(final_images_list[i])
        
        # Convert to tensor format
        if not output_images_list:
            raise ValueError("No output images generated")
        
        print(f"[CombineVideo] Generated {len(output_images_list)} total output images")
        
        try:
            image_tensor = self.frames_to_tensor(output_images_list)
            
            print(f"[CombineVideo] Image tensor shape: {image_tensor.shape}")
            print(f"[CombineVideo] Video combination completed successfully")
            
            return (image_tensor,)
            
        except Exception as e:
            print(f"[CombineVideo] Error creating tensor: {str(e)}")
            raise ValueError(f"Error creating output tensor: {str(e)}")

# ComfyUI Node Registration
NODE_CLASS_MAPPINGS = {
    "CombineVideoClips": CombineVideoClips
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CombineVideoClips": "Combine Video Clips"
}

# Note: Users can now input video paths by:
# 1. Connecting string nodes (like "String Literal" or "Text" nodes) to the video path inputs
# 2. Typing the full file paths directly into the text fields when not connected
# 3. Using ComfyUI's input folder system by placing videos in the input directory
# 4. Creating a custom web extension for file picker functionality