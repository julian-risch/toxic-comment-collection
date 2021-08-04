from . import dataset
from . import helpers
import os
import pandas as pd


class Wulczyn2017attack(dataset.Dataset):
    
    name = "wulczyn2017attack"
    url = "https://ndownloader.figshare.com/articles/4054689/versions/6"
    hash = "9e48068af1fbbe893af4df1b629ceebf924dc723a290c7bc473d2a8a8aac3529"
    files = [
        {
            "name": "wulczyn2017en_attack.csv",
            "language": "en",
            "type": "training",
            "platform": "wikipedia"
        }
    ]
    license = """ """

    @classmethod
    def valid_hash(cls, file):
        """do not check hash since it differs for each download"""
        return
        
    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        file1 = helpers.clean_csv(os.path.join(tmp_file_path, "attack_annotated_comments.tsv"), sep="\t")
        file2 = helpers.clean_csv(os.path.join(tmp_file_path, "attack_annotations.tsv"), sep="\t")
        
        df1 = pd.read_csv(file1)
        df1['comment'] = df1['comment'].apply(lambda x: x.replace("NEWLINE_TOKEN", " "))
        df1['comment'] = df1['comment'].apply(lambda x: x.replace("TAB_TOKEN", " "))
        df1.to_csv(file1 + "_endings", index=False)

        df2 = pd.read_csv(file2)
        labels = df2.groupby(["rev_id"]).mean() > 0.5
        labels.to_csv(file2 + "_grouped")

        tmp_file_path = helpers.join_csvs(file1 + "_endings", "rev_id", file2 + "_grouped", "rev_id")
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "wulczyn2017en_attack.csv"))
        
    @classmethod
    def unify_row(cls, row):
        row["text"] = row["comment"]
        labels = []
        if row["attack"]:
            labels.append("attack")
        else:
            labels.append("none")
        row["labels"] = labels
        row = row.drop(["rev_id","comment","year","logged_in","ns","sample","split","worker_id","quoting_attack","recipient_attack","third_party_attack","other_attack","attack"])
        return row
           