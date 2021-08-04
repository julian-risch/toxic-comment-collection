from . import dataset
from . import helpers
import os


class Sigurbergsson2019(dataset.Dataset):
    
    name = "sigurbergsson2019"
    url = "https://ndownloader.figshare.com/files/22476731"
    hash = "fb5c41c385062af222f68c8eb298912644b2f7a86d91769451a26c081f6822f0"
    files = [
        {
            "name": "sigurbergsson2019da.csv",
            "language": "da",
            "type": "training",
            "platform": "unknown"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        # read write to convert csv seperator to ","
        helpers.untarbz_file(tmp_file_path)
        tmp_file_path = os.path.join(os.path.dirname(tmp_file_path), "dkhate/oe20da_data/offenseval-da-training-v1.tsv")
        tmp_file_path = helpers.clean_csv(tmp_file_path, sep="\t")
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "sigurbergsson2019da.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["tweet"]
        if (row["subtask_a"] != "OFF" and row["subtask_a"] != "NOT"):
            row["labels"] = []
        else:
            row["labels"] = [row["subtask_a"]]
        row = row.drop(["id", "tweet", "subtask_a"])
        return row