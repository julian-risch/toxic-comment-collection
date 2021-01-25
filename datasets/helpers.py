import os
import shutil
import zipfile
import pandas as pd
from io import BytesIO
from urllib.request import urlopen

def download_from(url : str, destination_folder : str, file_name : str = "downloaded.file") -> str:
    with urlopen(url) as response:
        file_path = os.path.join(destination_folder, file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(response, f)
    return file_path

def convert_excel_to_csv(file_name : str) -> str:
    new_file = file_name + ".csv"
    excel_data = pd.read_excel(file_name)
    excel_data.to_csv(new_file)
    return new_file

def copy_file(source_file : str, destination_file : str):
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
    shutil.copyfile(source_file, destination_file)
    return destination_file

def unzip_file(file_name : str):
    extraction_dir = os.path.join(os.path.dirname(file_name), os.path.basename(file_name) + "_extracted")
    os.makedirs(extraction_dir, exist_ok=False)
    with zipfile.ZipFile(file_name) as zip_file:
        zip_file.extractall(extraction_dir)
    return extraction_dir