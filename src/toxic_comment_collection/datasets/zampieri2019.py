from . import dataset
from . import helpers
import os


class Zampieri2019(dataset.Dataset):
    
    name = "zampieri2019"
    url = "https://github.com/idontflow/OLID/raw/master/olid-training-v1.0.tsv"
    hash = "907e186e75876f1a77aeff72c97c988bdcd533493926567f7206da6f82f45ae9"
    files = [
        {
            "name": "zampieri2019en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, sep="\t")
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "zampieri2019en.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["tweet"]
        row["labels"] = [row["subtask_a"]]
        row = row.drop(["id", "tweet", "subtask_a", "subtask_b", "subtask_c"])
        return row