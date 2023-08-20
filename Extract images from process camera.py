# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:17:18 2023

@author: DELL
"""

import os
import cv2

# Set the path to the folder containing the videos
video_folder = 'J:\Jp\Gowtham\ResearchIR\Process Camera Data\procss\Gowtham-SS316'

# Set the path to the folder where you want to save the extracted frames
output_folder = 'J:\Jp\Gowtham\ResearchIR\Process Camera Data\Extraction'

# Get a list of all video files in the folder
video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    
    # Create a folder with the same name as the video (without extension)
    video_name = os.path.splitext(video_file)[0]
    output_video_folder = os.path.join(output_folder, video_name)
    os.makedirs(output_video_folder, exist_ok=True)
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save the frame to the output folder
        frame_filename = f"{video_name}_frame_{frame_count:04d}.jpg"
        frame_path = os.path.join(output_video_folder, frame_filename)
        cv2.imwrite(frame_path, frame)
        
        frame_count += 1
    
    # Release the video capture object
    cap.release()

print("Frame extraction completed.")