from . import dataset
from . import helpers
import os
import pandas as pd
class Mulki2019(dataset.Dataset):
    
    name = "mulki2019"
    url = "https://github.com/Hala-Mulki/L-HSAB-First-Arabic-Levantine-HateSpeech-Dataset/raw/master/Dataset/L-HSAB"
    hash = "3fc5e06ab624b47e404a0530388631c4894c323ca038e726ce6dd3d0e6a371e3"
    files = [
        {
            "name": "mulki2019ar.csv",
            "language": "ar",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        # read write to convert csv seperator to ","
        df = pd.read_csv(tmp_file_path, sep="\t")
        df.to_csv(tmp_file_path, index=False)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "mulki2019ar.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["Tweet"]
        labels = [row["Class"]]
        row["labels"] = labels
        row = row.drop(["Class", "Tweet"])
        return row