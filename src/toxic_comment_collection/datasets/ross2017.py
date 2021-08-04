from . import dataset
from . import helpers
import os


class Ross2017(dataset.Dataset):
    
    name = "ross2017"
    url = "https://github.com/UCSM-DUE/IWG_hatespeech_public/raw/master/german%20hatespeech%20refugees.csv"
    hash = "b0784b8c00f02d16cee8b1227b8e8968760885d3d87b68762ba51b4c3156714f"
    files = [
        {
            "name": "ross2018de.csv",
            "language": "de",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""
    
    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "ross2018de.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["Tweet"]
        labels = []
        if (row["HatespeechOrNot (Expert 1)"] == "YES" or row["HatespeechOrNot (Expert 2)"] == "YES"):
            labels.append("hate")
        else:
            labels.append("nohate")
        row["labels"] = labels
        row = row.drop(["Tweet","HatespeechOrNot (Expert 1)","HatespeechOrNot (Expert 2)","Hatespeech Rating (Expert 2)"])
        return row