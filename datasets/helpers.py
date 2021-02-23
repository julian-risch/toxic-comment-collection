import os
import shutil
import zipfile
import pandas as pd
import json
from io import BytesIO
from urllib.request import urlopen
from twarc import Twarc

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
    excel_data.to_csv(new_file, index=False)
    return new_file

def copy_file(source_file : str, destination_file : str) -> str:
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)
    shutil.copyfile(source_file, destination_file)
    return destination_file

def convert_json_to_csv(file_name : str) -> str:
    new_file = file_name + ".csv"
    json_data = pd.read_json(file_name)
    json_data.to_csv(new_file, index=False)
    return new_file

def convert_jsonl_to_csv(file_name : str) -> str:
    new_file = file_name + ".json"
    data = []
    with open(file_name, "r") as jsonl_file:
        for line in jsonl_file:
            data.append(json.loads(line))
    df = pd.DataFrame(data)
    df.to_csv(new_file, index=False)
    return new_file

def unzip_file(file_name : str):
    extraction_dir = os.path.join(os.path.dirname(file_name), os.path.basename(file_name) + "_extracted")
    os.makedirs(extraction_dir, exist_ok=False)
    with zipfile.ZipFile(file_name) as zip_file:
        zip_file.extractall(extraction_dir)
    return extraction_dir

def add_column(file_name : str, column_name : str, column_value) -> str:
    new_file = file_name + "_new_column"
    df = pd.read_csv(file_name)
    df.insert(loc=0, column=column_name, value=[column_value] * df.count().tweet_id)
    df.to_csv(new_file, index=False)
    return new_file

def clean_csv(file_name : str, names : [str] = None ) -> str:
    new_file = file_name + "_clean"
    df = pd.read_csv(file_name, names=names)
    df.to_csv(new_file, index=False)
    return new_file

def download_tweets_for_csv(file_name : str, column : str) -> str:
    def hydrate(row, translation):
        if row[column] in translation:
            row["text"] = translation[row[column]]
            row = row.drop(column)
            return row
        return None

    new_file = file_name + "_with_tweets"
    df = pd.read_csv(file_name)
    with open("config.json", "r") as config:
        api_data = json.load(config)
    t = Twarc(
        api_data["consumer_key"],
        api_data["consumer_secret"],
        api_data["access_token"],
        api_data["access_token_secret"]
        )
    print(df)
    translation = {}
    for tweet in t.hydrate(df[column]):
        translation[tweet["id"]] = tweet["full_text"]
    df = df.apply(hydrate, axis=1, args=(translation,)).dropna()
    df.to_csv(new_file, index=False)
    return new_file
