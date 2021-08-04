from . import dataset
import os
from . import helpers


class Founta2018(dataset.Dataset):
    
    name = "founta2018"
    url = "https://zenodo.org/record/2657374/files/hatespeech_id_label.csv"
    hash = "35f19a5746eac9be27cd635a09b9ced11569080df10d84fb140ca76164836cef"
    files = [
        {
            "name": "founta2018en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """ """
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, names=["tweet", "class"])
        tmp_file_path = helpers.download_tweets_for_csv(tmp_file_path, "tweet", api_config)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "founta2018en.csv"))

    @classmethod
    def unify_row(cls, row):
        row["labels"] = [row["class"]]
        row = row.drop(["class"])
        return row