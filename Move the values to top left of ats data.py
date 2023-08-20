# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 14:34:29 2023

@author: DELL
"""


import os
import pandas as pd

# Specify the parent folder containing 120 main folders
parent_folder = r'J:\Jp\Gowtham\ResearchIR\ResearchIR Excel and analysis'

# Function to remove rows and columns with no values from a DataFrame
def remove_empty_rows_columns(df):
    df.dropna(axis=0, how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    return df

# Iterate through main folders
for main_folder_name in os.listdir(parent_folder):
    main_folder_path = os.path.join(parent_folder, main_folder_name)
    
    # Check if the item is indeed a directory
    if os.path.isdir(main_folder_path):
        excel_new_folder_path = os.path.join(main_folder_path, 'excel_new')
        
        # Check if the "excel_new" subfolder exists
        if os.path.exists(excel_new_folder_path) and os.path.isdir(excel_new_folder_path):
            print(f"Processing main folder: {main_folder_name}")
            
            # Iterate through subfolders (track_1, track_2, track_3) within "excel_new"
            for track_folder_name in os.listdir(excel_new_folder_path):
                track_folder_path = os.path.join(excel_new_folder_path, track_folder_name)
                
                # Check if the item is indeed a directory
                if os.path.isdir(track_folder_path):
                    print(f"Processing track folder: {track_folder_name}")
                    
                    # Iterate through CSV files in the track folder
                    for csv_filename in os.listdir(track_folder_path):
                        if csv_filename.endswith('.csv'):
                            csv_file_path = os.path.join(track_folder_path, csv_filename)
                            
                            # Read the CSV file using pandas
                            df = pd.read_csv(csv_file_path)
                            
                            # Remove empty rows and columns
                            df = remove_empty_rows_columns(df)
                            
                            # Save the modified DataFrame back to the same CSV file
                            df.to_csv(csv_file_path, index=False)
                            
                            print(f"Processed: {csv_filename}")
            
print("Process complete.")





