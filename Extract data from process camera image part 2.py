# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:29:21 2023

@author: DELL
"""

import os
import glob
import time
import pytesseract
from PIL import Image
import pandas as pd

# Initialize the Tesseract path (modify as needed)
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def extract_text_from_image(image_path, top, bottom):
    im = Image.open(image_path)
    width, height = im.size
    left = 1150
    right = 1265
    
    im1 = im.crop((left, top, right, bottom))
    im1 = im1.resize((500, 100))
    
    custom_config = r'-l eng --oem 1 --psm 6'
    text = pytesseract.image_to_string(im1, config=custom_config)
    return text.strip()  # Remove leading/trailing whitespace

# Set the base path to the root folder containing the image folders
base_path = 'J:\Jp\Gowtham\ResearchIR\Process Camera Data\procss\TEST'

# Get a list of subdirectories (each representing a folder)
folder_names = next(os.walk(base_path))[1]

# Define the regions (top, bottom) for text extraction
regions = [
    (100, 118),
    (113, 130),
    (127, 145),
    (141, 160),
    (155, 177),
    (182, 202),
    (200, 217),
    (211, 230),
    (225, 242),
    (240, 258),
    (253, 274),
    (270, 287),
    (282, 300),
    (300, 310),
    (310, 330),
    (325, 343),
    (338, 358),
    (357, 372),
    (367, 385)
]

total_start_time = time.time()

for folder_name in folder_names:
    image_folder = os.path.join(base_path, folder_name)
    print(image_folder)
    # Get a list of all image files in the folder
    image_files = glob.glob(os.path.join(image_folder, '*.jpg'))

    # Create a list to store dictionaries for each image
    data_list = []

    folder_start_time = time.time()

    for image_file in image_files:
        image_name = os.path.basename(image_file)
        # Extract text from multiple regions using the previous code
        text_list = [extract_text_from_image(image_file, top, bottom) for top, bottom in regions]
        
        # Create a dictionary for the current image
        image_data = {'Image Name': image_name}
        for i, text in enumerate(text_list):
            region_name = f'Region {i + 1}'
            image_data[region_name] = text

        data_list.append(image_data)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data_list)
    
    # Rename the columns
    new_columns = {
        f'Region {i + 1}': column_name
        for i, column_name in enumerate([
            'Area', 'centroid X', 'centroid Y', 'Perimeter', 'Form factor', 'BB left',
            'BB top', 'BB width', 'BB height', 'Orientation', 'Eccentricity', 'Euler number',
            'Hole count', 'Touches border', 'Feret diam 0', 'Feret diam 90', 'Gray mass',
            'Gray mean', 'Compactness'
        ])
    }
    df = df.rename(columns=new_columns)


    # Create an Excel writer and save the DataFrame to Excel
    excel_path = os.path.join(image_folder, 'extracted_text.xlsx')
    df.to_excel(excel_path, index=False)

    folder_end_time = time.time()
    folder_duration = folder_end_time - folder_start_time
    print(f"Text extraction and Excel saving completed for folder: {folder_name} | Time: {folder_duration:.2f} seconds")

total_end_time = time.time()
total_duration = total_end_time - total_start_time
print(f"Total time taken: {total_duration:.2f} seconds")