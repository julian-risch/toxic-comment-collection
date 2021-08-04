from . import dataset
from . import helpers
import os


class Mathur2018(dataset.Dataset):
    
    name = "mathur2018"
    url = "https://github.com/pmathur5k10/Hinglish-Offensive-Text-Classification/raw/master/Hinglish_Profanity_List.csv"
    hash = "e09ccb2c46616a59faa5d80d205a6e49b01b4781c1eb31587e1098a86c751260"
    files = [
        {
            "name": "mathur2018hing.csv",
            "language": "hing",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, names=["text", "translation", "class"])
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "mathur2018hing.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = ["hate:" + str(row["class"])]
        row["labels"] = labels
        row = row.drop(["translation", "class"])
        return row