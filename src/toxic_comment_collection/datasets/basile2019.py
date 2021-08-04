from . import dataset
from . import helpers
import os


class Basile2019(dataset.Dataset):
    
    name = "basile2019"
    url = "https://github.com/cicl2018/HateEvalTeam/raw/master/Data%20Files/Data%20Files/%232%20Development-English-A/train_dev_en_merged.tsv"
    hash = "fdd34bf56f0afa744ee7484774d259d83a756033cd8049ded81bd55d2fcb1272"
    files = [
        {
            "name": "basile2019en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """HS - a binary value indicating if HS is occurring against one of the given targets (women or immigrants): 1 if occurs, 0 if not.
Target Range - if HS occurs (i.e.  the value for the feature HS is 1), a binary value indicating if the target is a generic group of people (0) or a specific individual (1).
Aggressiveness- if HS occurs (i.e. the value for  the  feature  HS  is  1),  a  binary  value  indicating  if  the  tweeter  is  aggressive  (1)  or not (0)."""
    license = """"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, sep='\t')
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "basile2019en.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = []
        if row["HS"] == 1:
            labels.append("HS")
        if row["TR"] == 1:
            labels.append("TR")
        if row["AG"] == 1:
            labels.append("AG")
        row["labels"] = labels
        row = row.drop(["HS","TR","AG","id"])
        return row