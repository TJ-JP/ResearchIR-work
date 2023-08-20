# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 18:32:29 2023

@author: DELL
"""

import os
import pandas as pd

# Specify the folder containing CSV files
parent_folder = 'J:\Jp\Gowtham\ResearchIR\ResearchIR Excel and analysis'

# Specify the value to remove
value_to_remove = 1410.337

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
                    
                    # Read the CSV file with header=None
                    df = pd.read_csv(file_path, header=None)
                    df = df.iloc[1:]
                    # Remove the specified value
                    min_value = df.min().min()
                    df = df[df != min_value]
                    print(df)
                    # Save the updated DataFrame back to the CSV file
                    df.to_csv(file_path, index=False, header=False)
                   # print(f"Processed: {filename} in main folder: {main_folder_name}")
                    # Check if the minimum value is less than 1410
                    print(f"Minimum value {min_value} removed in Folder: {main_folder_name}, File: {filename}")

print("Process complete.")