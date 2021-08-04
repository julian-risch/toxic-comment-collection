from . import dataset
from . import helpers
import os


class Kumar2018(dataset.Dataset):
    
    name = "kumar2018"
    url = "https://github.com/SilentFlame/AggressionDetection/raw/master/DataPre-Processing/processedDataWithoutID.txt"
    hash = "06154c3f8b85254af949e3e83aca32c1b4e25af322f18221a58d02453132dd48"
    files = [
        {
            "name": "kumar2018hing.csv",
            "language": "hing",
            "type": "training",
            "platform": "facebook"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, names=["text", "class"], sep="\t")
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "kumar2018hing.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = [row["class"]]
        row["labels"] = labels
        row = row.drop(["class"])
        return row