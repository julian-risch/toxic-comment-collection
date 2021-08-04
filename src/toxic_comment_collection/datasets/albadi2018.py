from typing import Dict

from . import dataset
from . import helpers
import os


class Albadi2018(dataset.Dataset):
    
    name = "albadi2018"
    url = "https://github.com/nuhaalbadi/Arabic_hatespeech/archive/refs/heads/master.zip"
    hash = "7f7d87384b4b715655ec0e2d329bc234bbc965ad116290f2e2d0b11e26e272b3"
    files = [
        {
            "name": "albadi2018ar_train.csv",
            "language": "ar",
            "type": "training",
            "platform": "twitter"
        },
        {
            "name": "albadi2018ar_test.csv",
            "language": "ar",
            "type": "test",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        file_dir = helpers.unzip_file(tmp_file_path)
        train_file = helpers.download_tweets_for_csv(os.path.join(file_dir, "Arabic_hatespeech-master/train.csv"), "id", api_config)
        test_file = helpers.download_tweets_for_csv(os.path.join(file_dir, "Arabic_hatespeech-master/test.csv"), "id", api_config)
        helpers.copy_file(train_file, os.path.join(dataset_folder, "albadi2018ar_train.csv"))
        helpers.copy_file(test_file, os.path.join(dataset_folder, "albadi2018ar_test.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = []
        if row["hate"] == 1:
            labels.append("hate")
        else:
            labels.append("noHate")
        row["labels"] = labels
        row = row.drop(["hate"])
        return row