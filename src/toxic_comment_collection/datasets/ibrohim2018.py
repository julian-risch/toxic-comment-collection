from . import dataset
import os
from . import helpers


class Ibrohim2018(dataset.Dataset):
    
    name = "ibrohim2018"
    url = "https://github.com/okkyibrohim/id-abusive-language-detection/raw/master/re_dataset_three_labels.csv"
    hash = "8e88d5bf4d98f86d7c8fb9c010008246e206814e8dbe5695ec7de4a76812bc86"
    files = [
        {
            "name": "ibrohim2018id.csv",
            "language": "id",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """1 (not abusive language), 2 (abusive but not offensive), and 3 (offensive language)"""
    license = """This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License."""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "ibrohim2018id.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["Tweet"]

        labels = []
        if row["Label"] == 1:
            labels.append("none")
        if row["Label"] == 2:
            labels.append("abusive")
        if row["Label"] == 3:
            labels.append("offensive")
        
        row["labels"] = labels
        row = row.drop(["Tweet","Label"])
        return row