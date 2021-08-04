from . import dataset
import os
from . import helpers


class Fortuna2019(dataset.Dataset):
    
    name = "fortuna2019"
    url = "https://b2share.eudat.eu/api/files/792b86e1-e676-4a0d-971f-b41a1ffb9b18/annotator_classes.csv"
    hash = "f759888e9489a030187bbf6fbe005a7c5a6c0c3468882430924d9aaebd84759d"
    files = [
        {
            "name": "fortuna2019pt.csv",
            "language": "pt",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """ """
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.download_tweets_for_csv(tmp_file_path, "tweet_id", api_config)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "fortuna2019pt.csv"))

    @classmethod
    def unify_row(cls, row):

        labels = row["class"].split("; ")
       
        row["labels"] = labels
        row = row.drop(["class"])
        return row