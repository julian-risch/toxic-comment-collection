from . import dataset
from . import helpers
import os

class Kulkarni2021(dataset.Dataset):
    
    name = "kulkarni2021"
    url = "https://github.com/l3cube-pune/MarathiNLP/raw/main/L3CubeMahaSent%20Dataset/tweets-train.csv"
    hash = "1416e35f859f7473c536432954affe6460fad7a0a0d2c3889ce7a408347832d5"
    files = [
        {
            "name": "kulkarni2021mr.csv",
            "language": "mr",
            "type": "training",
            "platform": "tweets"
        }
    ]
    comment = """Positive(1), Negative(-1) and Neutral(0)"""

    license = """"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "kulkarni2021mr.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["tweet"]
        row["labels"] = [str(row["label"])]
        row = row.drop(["tweet", "label"])
        return row
