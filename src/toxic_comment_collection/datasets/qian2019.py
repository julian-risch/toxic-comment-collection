from . import dataset
from . import helpers
import os
import pandas as pd
import json

class Qian2019(dataset.Dataset):
    
    name = "qian2019"
    url = "https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech/archive/master.zip"
    hash = "e2774f61af64942373e76e3928269bf6b7d8b41d5f5dcbcac9e760d4e93ef6b4"
    files = [
        {
            "name": "qian2019en_gab.csv",
            "language": "en",
            "type": "training",
            "platform": "gab"
        },
        {
            "name": "qian2019en_reddit.csv",
            "language": "en",
            "type": "training",
            "platform": "reddit"
        }
    ]
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        helpers.copy_file(os.path.join(tmp_file_path, "A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech-master/data/gab.csv"), os.path.join(dataset_folder, "qian2019en_gab.csv"))
        helpers.copy_file(os.path.join(tmp_file_path, "A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech-master/data/reddit.csv"), os.path.join(dataset_folder, "qian2019en_reddit.csv"))

    @classmethod
    def unify_format(cls, df):
        df = df.fillna({"hate_speech_idx":"[]"})
        clean_data = []
        for i,row in df.iterrows():
            for idx,comment in enumerate(row["text"].split("\n")):
                labels = []
                if idx+1 in json.loads(row["hate_speech_idx"]):
                    labels.append("hate")
                if comment:
                    clean_data.append({"text": comment, "labels": labels})
        return pd.DataFrame(clean_data)
           