# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:57:13 2023

@author: DELL
"""

import os
import pandas as pd

root_folder = "J:\\Jp\\Gowtham\\ResearchIR\\Process Camera Data\\procss\\Extracted images\\This computer\\three"


for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)
    
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            
            file_path = os.path.join(folder_path, file_name)
            print(file_path)
            if file_name.lower().endswith('.xlsx') or file_name.lower().endswith('.xls'):
                df = pd.read_excel(file_path)
                
                # Convert the 'Area' column to numeric (removing commas)
                df['centroid X'] = pd.to_numeric(df['Area'].str.replace(',', ''), errors='coerce')
                
                # Filter out rows with non-positive area values
                df = df[df['centroid X'] > 0]
                new_file_path = file_path.replace('.xlsx', '_filtered.xlsx')
                with pd.ExcelWriter(new_file_path, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, sheet_name='Sheet1')
                
                # Remove the original file and replace it with the filtered one
                os.remove(file_path)
                os.rename(new_file_path, file_path)