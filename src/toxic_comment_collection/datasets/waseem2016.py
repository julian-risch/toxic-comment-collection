from . import dataset
from . import helpers
import os


class Waseem2016(dataset.Dataset):
    
    name = "waseem2016"
    url = "https://github.com/ZeerakW/hatespeech/raw/master/NAACL_SRW_2016.csv"
    hash = "a23875e68792a9d66cafea3c1c42b0b563b35fbd6163a66c3c4451976ebcdcff"
    files = [
        {
            "name": "waseem2016en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        },
    ]
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, ["twitter_ids", "tag"])
        tmp_file_path = helpers.download_tweets_for_csv(tmp_file_path, "twitter_ids", api_config)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "waseem2016en.csv"))

    @classmethod
    def unify_row(cls, row):
        row["labels"] = [row["tag"]]
        row = row.drop(["tag"])
        return row
