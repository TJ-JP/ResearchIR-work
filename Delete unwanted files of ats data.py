# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 11:04:33 2023

@author: DELL
"""
import os
import pandas as pd
import time
import re

# Specify the parent folder containing 100 main folders
parent_folder = 'J:\Jp\Gowtham\ResearchIR\ResearchIR Excel and analysis'

# Get the current time at the start of the process
start_time = time.time()

# Function to check if a file contains the number "1"
def contains_number_one(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return '1' in content

# Iterate through main folders
for main_folder_name in os.listdir(parent_folder):
    main_folder_path = os.path.join(parent_folder, main_folder_name)
    
    # Check if the item is indeed a directory
    if os.path.isdir(main_folder_path):
        excel_subfolder_path = os.path.join(main_folder_path, 'excel')
        
        # Check if the "excel" subfolder exists
        if os.path.exists(excel_subfolder_path) and os.path.isdir(excel_subfolder_path):
            print(f"Processing main folder: {main_folder_name}")
            
            # Iterate through CSV files in the "excel" subfolder
            for filename in os.listdir(excel_subfolder_path):
                if filename.endswith('.csv'):
                    file_path = os.path.join(excel_subfolder_path, filename)
                    
                    # Check if the file contains the number "1"
                    if not contains_number_one(file_path):
                        print(f"Removing file with no '1': {file_path}")
                        os.remove(file_path)
            
# Get the current time at the end of the process
end_time = time.time()

# Calculate the total time taken for the process
total_time = end_time - start_time

print(f"Process complete. Total time taken: {total_time:.2f} seconds.")