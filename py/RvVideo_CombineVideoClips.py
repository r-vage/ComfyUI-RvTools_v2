import os
import cv2
import numpy as np
import torch
from PIL import Image
from ..core import CATEGORY, cstr

FPS = float(30.0)

class RvVideo_CombineVideoClips:
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

                "simple_combine": ("BOOLEAN", {
                    "default": False,
                    "tooltip": "When True it combines the video files only (without join files)"
                }),
            },
            "optional": {
                "video_filelist": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                }),
                "joined_filelist": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "display": "text",
                }),
            }
        }
    
    RETURN_TYPES = ("IMAGE", "FLOAT")
    RETURN_NAMES = ("image", "fps")
    FUNCTION = "combine_videos"
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value
    
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
        FPS = cap.get(cv2.CAP_PROP_FPS)

        cstr(f"Video {video_path}: {total_frames} frames, {FPS} fps").msg.print()
                
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
        
        cstr(f"Successfully loaded {len(frames)} frames from {video_path}").msg.print()
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
    
    def combine_videos(self, frame_load_cap, simple_combine, video_filelist=None, joined_filelist=None):
        """Main processing function that combines the video clips"""

        if not video_filelist in (None, '', 'undefined', 'none') : 
            videos = video_filelist.split(', ')

            #for i in range (len(videos)):
            #    print(f"  video file: {videos[i]}")
            
        if not joined_filelist in (None, '', 'undefined', 'none') : 
            joined = joined_filelist.split(', ')

            #for i in range (len(joined)):
            #    print(f"  joined file: {joined[i]}")

        output_images_list = []

        if videos and not simple_combine:                
            video_first = str(videos[0]).strip()
            video_last =  str(videos[-1]).strip()

            print(f"  video_first: {video_first}")
            print(f"  video_last: {video_last}")

            # Check if required files exist
            if not os.path.exists(video_first):
                raise ValueError(f"First video file not found: {video_first}")
            if not os.path.exists(video_last):
                raise ValueError(f"Last video file not found: {video_last}")

            try:
                # Load first video (required)
                first_images_list = self.load_video_frames(video_first, frame_load_cap)
                final_images_list = self.load_video_frames(video_last, frame_load_cap)
                joined_images_list = []

                if joined:
                    for i in range (len(joined)):
                        video_join = str(joined[i]).strip()

                        if os.path.exists(video_join):
                            joined_images_list.extend(self.load_video_frames(video_join))          
                            cstr(f"total frames loaded: {len(joined_images_list)}").msg.print()
            
            except Exception as e:
                cstr(f"Error loading video frames: {str(e)}").error.print()
                raise ValueError(f"Error loading video frames: {str(e)}")

            # g: Store 0 in first_images_start_index
            first_images_start_index = 0
            
            # h: Calculate frame_load_cap // 2 and store in first_images_end_index
            first_images_end_index = frame_load_cap // 2 
            
            # Ensure indices are within bounds
            first_images_end_index = min(first_images_end_index, len(first_images_list))
            
            # i: Append images from first_images_list to output_images_list
            cstr(f"Adding first video frames [{first_images_start_index}:{first_images_end_index}]").msg.print()
            for i in range(first_images_start_index, first_images_end_index):
                if i < len(first_images_list):
                    output_images_list.append(first_images_list[i])
            
            # j: If first_joined_images_list is not empty, append all its images
            if joined_images_list:
                cstr(f"Adding joined video frames: {len(joined_images_list)}").msg.print()
                output_images_list.extend(joined_images_list)

            # o: Calculate frame_load_cap // 2 and store in final_images_start_index
            final_images_start_index = frame_load_cap // 2
            
            # Ensure start index is within bounds
            final_images_start_index = min(final_images_start_index, len(final_images_list))
            
            # p: Append images from final_images_list starting from final_images_start_index to end
            cstr(f"Adding final video frames [{final_images_start_index}:{len(final_images_list)}]").msg.print()
            for i in range(final_images_start_index, len(final_images_list)):
                output_images_list.append(final_images_list[i])
        
        elif videos and simple_combine:
            
            for i in range (len(videos)):
                video = str(videos[i]).strip()

                if os.path.exists(video):
                    try:
                        output_images_list.extend(self.load_video_frames(video))          
                        cstr(f"total frames loaded: {len(output_images_list)}").msg.print()

                    except Exception as e:
                        cstr(f"Error loading video frames: {str(e)}").error.print()
                        raise ValueError(f"Error loading video frames: {str(e)}")                    
    
        # Convert to tensor format
        if not output_images_list:
            raise ValueError("No output images generated")
        
        cstr(f"Generated {len(output_images_list)} total output images").msg.print()
        
        try:
            image_tensor = self.frames_to_tensor(output_images_list)
            
            cstr(f"Image tensor shape: {image_tensor.shape}").msg.print()
            cstr(f"Video combination completed successfully").msg.print()
            
            return (image_tensor, FPS,)
            
        except Exception as e:
            cstr(f"Error creating tensor: {str(e)}").msg.print()
            raise ValueError(f"Error creating output tensor: {str(e)}")

NODE_NAME = 'Combine Video Clips v2 [RvTools]'
NODE_DESC = 'Combine Video Clips v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvVideo_CombineVideoClips
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
