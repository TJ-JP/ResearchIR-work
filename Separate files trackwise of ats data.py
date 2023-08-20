# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 12:39:57 2023

@author: DELL
"""

import os
import shutil
import time

# Specify the parent folder containing 100 main folders
parent_folder = 'J:\Jp\Gowtham\ResearchIR\ResearchIR Excel and analysis'

# Function to extract the number from a file name
def extract_number(filename):
    return int(filename.split('.')[0])  # Assuming the file extension is ".csv"

# Function to determine the track for a given file number
def determine_track(file_number, track_ranges):
    for track_index, (start, end) in enumerate(track_ranges, start=1):
        if start <= file_number <= end:
            return track_index
    return None

# Get the current time at the start of the process
start_time = time.time()

# Iterate through main folders
for main_folder_name in os.listdir(parent_folder):
    main_folder_path = os.path.join(parent_folder, main_folder_name)
    
    # Check if the item is indeed a directory
    if os.path.isdir(main_folder_path):
        excel_subfolder_path = os.path.join(main_folder_path, 'excel')
        excel_new_subfolder_path = os.path.join(main_folder_path, 'excel_new')  # Define the excel_new_subfolder_path
        
        # Check if the "excel" subfolder exists
        if os.path.exists(excel_subfolder_path) and os.path.isdir(excel_subfolder_path):
            print(f"Processing main folder: {main_folder_name}")
            
            # Get the list of files in the "excel" subfolder
            files = [filename for filename in os.listdir(excel_subfolder_path) if filename.endswith('.csv')]
            
            # Sort the list of files based on the extracted numbers
            sorted_files = sorted(files, key=extract_number)
            
            # Initialize track ranges
            track_ranges = []
            
            # Iterate through the sorted files and determine track ranges based on gaps
            current_range_start = None
            current_range_end = None
            
            for filename in sorted_files:
                file_number = extract_number(filename)
                
                if current_range_start is None:
                    current_range_start = file_number
                    current_range_end = file_number
                elif file_number - current_range_end <= 10:
                    current_range_end = file_number
                else:
                    track_ranges.append((current_range_start, current_range_end))
                    current_range_start = file_number
                    current_range_end = file_number
            
            # Add the final track range
            if current_range_start is not None:
                track_ranges.append((current_range_start, current_range_end))
                
            # Remove files with single-number track ranges
            for track_start, track_end in track_ranges:
                if track_start == track_end:
                    file_to_remove = f"{track_start}.csv"
                    file_path = os.path.join(excel_subfolder_path, file_to_remove)
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        print(f"Removed file: {file_to_remove}")
            
            # Iterate through files in the "excel" subfolder and categorize them into track subfolders
            for filename in sorted_files:
                file_number = extract_number(filename)
                track = determine_track(file_number, track_ranges)
               
                if track is not None:
                    track_folder = os.path.join(excel_new_subfolder_path, f'{track}')
                    os.makedirs(track_folder, exist_ok=True)
                    
                    source_path = os.path.join(excel_subfolder_path, filename)
                    target_path = os.path.join(track_folder, filename)
                    shutil.move(source_path, target_path)
print("Process complete.")