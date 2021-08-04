from . import dataset
from . import helpers
import os
import json
import pandas as pd

class Chung2019(dataset.Dataset):
    
    name = "chung2019"
    url = "https://github.com/marcoguerini/CONAN/raw/master/CONAN.json"
    hash = "511c062b5563affbc78bb2c9d9edafd88fe6419add73b5190865bb42863eacc4"
    files = [
        {
            "name": "chung2019.csv",
            "language": "en/fr/it",
            "type": "training",
            "platform": "artifical"
        }
    ]
    license = """This resource can be used for research purposes. Please cite the publication above if you use it."""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        with open(tmp_file_path, "r") as f:
            a = json.load(f)
        b = pd.DataFrame(a['conan'])
        tmp_file_path = tmp_file_path + ".csv"
        b.to_csv(tmp_file_path, index=False)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "chung2019.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["hateSpeech"]
        labels = ["hate"]
        labels.append(row["hsType"])
        row["labels"] = labels
        row = row.drop(["cn_id","age","gender","educationLevel","cnType","hsType","hsSubType","hateSpeech","counterSpeech"])
        return row

    @classmethod
    def unify_format(cls, df):
        df = df.apply(cls.unify_row, axis=1)
        return df.drop_duplicates(subset=["text"])
        