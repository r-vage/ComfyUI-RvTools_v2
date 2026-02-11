import os
import cv2   # type: ignore
import numpy as np   # type: ignore
import torch  # type: ignore
from PIL import Image
from ..core import CATEGORY, log

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
    
    CATEGORY = CATEGORY.MAIN.value + CATEGORY.VIDEO.value

    RETURN_TYPES = ("IMAGE", "FLOAT")
    RETURN_NAMES = ("image", "fps")
    FUNCTION = "combine_videos"
    
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

        log.msg("VideoClipsCombine", f"Video {video_path}: {total_frames} frames, {FPS} fps")
                
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
        
        log.msg("VideoClipsCombine", f"Successfully loaded {len(frames)} frames from {video_path}")
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
            #    print(f"  join file: {joined[i]}")

        output_images_list = []

        video_1_start_idx = 0
        video_1_end_idx = 0

        if videos and not simple_combine:                
            last_was_join = False

            for i in range (len(videos)):
                video_1_list = []
                video_join_list = []
                video_1_exists = False
                join_exists = False
                
                video_1 = str(videos[i]).strip()
                video_1_exists = os.path.exists(video_1)
                
                if last_was_join:
                    if joined: #list of join files
                        video_join = str(joined[i]).strip()   #both list have the same length but maybe a different start number but "i" should be the correct position anyways
                    
                    join_exists = os.path.exists(video_join)

                    if join_exists:
                        video_join_list.extend(self.load_video_frames(video_join))                
                        
                        if video_join_list:
                            output_images_list.extend(video_join_list)

                    else:
                        last_was_join = False
                        #no join file, last file was join, add 2nd half of video_1, this is the "last video" after the join file

                        if video_1_exists:
                            video_1_list = self.load_video_frames(video_1, frame_load_cap)

                        if video_1_list:
                            video_1_start_idx = frame_load_cap // 2
                            video_1_start_idx = min(video_1_start_idx, len(video_1_list))

                            video_1_end_idx = frame_load_cap 
                            video_1_end_idx = min(video_1_end_idx, len(video_1_list))

                            #Append images from video_1_list to output_images_list
                            log.msg("VideoClipsCombine", f"Adding Frames video_1 [{video_1_start_idx}:{video_1_end_idx}]")
                            
                            for i in range(video_1_start_idx, video_1_end_idx):
                                if i < len(video_1_list):
                                    output_images_list.append(video_1_list[i])

                else:
                    #load the first video (first half if a join file exists)
                    #check if a join file exists

                    if video_1_exists:
                        video_1_list = self.load_video_frames(video_1, frame_load_cap)

                    if joined: #list of join files
                        video_join = str(joined[i]).strip()   #both list have the same length but maybe a different start number but "i" should be the correct position anyways

                    join_exists = os.path.exists(video_join)

                    if join_exists:
                        video_join_list.extend(self.load_video_frames(video_join))                
                        
                        if video_1_list:
                            video_1_start_idx = 0
                            video_1_end_idx = frame_load_cap // 2 #trim video_1 to add the frames of the join file
                            video_1_end_idx = min(video_1_end_idx, len(video_1_list))

                            #Append images from video_1_list to output_images_list
                            log.msg("VideoClipsCombine", f"Adding Frames video_1 [{video_1_start_idx}:{video_1_end_idx}]")
                            
                            for i in range(video_1_start_idx, video_1_end_idx):
                                if i < len(video_1_list):
                                    output_images_list.append(video_1_list[i])

                        if video_join_list:
                            #If video_join_list is not empty, append all its images
                            log.msg("VideoClipsCombine", f"Adding Frames video_join: {len(video_join_list)}")
                            output_images_list.extend(video_join_list)
                            last_was_join = True


                    else:
                        #no join file add all frames of video_1
                        if video_1_list:
                            video_1_start_idx = 0
                            video_1_end_idx = frame_load_cap 
                            video_1_end_idx = min(video_1_end_idx, len(video_1_list))

                            # i: Append images from video_1_list to output_images_list
                            log.msg("VideoClipsCombine", f"Adding Frames video_1 [{video_1_start_idx}:{video_1_end_idx}]")
                            
                            for i in range(video_1_start_idx, video_1_end_idx):
                                if i < len(video_1_list):
                                    output_images_list.append(video_1_list[i])

        elif videos and simple_combine:
            
            for i in range (len(videos)):
                video = str(videos[i]).strip()

                if os.path.exists(video):
                    try:
                        output_images_list.extend(self.load_video_frames(video))          

                    except Exception as e:
                        log.error("VideoClipsCombine", f"Error loading video frames: {str(e)}")
                        raise ValueError(f"Error loading video frames: {str(e)}")                    
    
        # Convert to tensor format
        if not output_images_list:
            raise ValueError("No output images generated")
        
        log.msg("VideoClipsCombine", f"Generated {len(output_images_list)} total output images")
        
        try:
            image_tensor = self.frames_to_tensor(output_images_list)
            
            log.msg("VideoClipsCombine", f"Image tensor shape: {image_tensor.shape}")
            log.msg("VideoClipsCombine", f"Video combination completed successfully")
            
            return (image_tensor, FPS,)
            
        except Exception as e:
            log.msg("VideoClipsCombine", f"Error creating tensor: {str(e)}")
            raise ValueError(f"Error creating output tensor: {str(e)}")

NODE_NAME = 'Combine Video Clips v2 [RvTools]'
NODE_DESC = 'Combine Video Clips v2'

NODE_CLASS_MAPPINGS = {
   NODE_NAME: RvVideo_CombineVideoClips
}

NODE_DISPLAY_NAME_MAPPINGS = {
    NODE_NAME: NODE_DESC
}
