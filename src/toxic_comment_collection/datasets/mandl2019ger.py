from . import dataset
from . import helpers
import os


class Mandl2019ger(dataset.Dataset):
    
    name = "mandl2019ger"
    url = "https://hasocfire.github.io/hasoc/2019/files/german_dataset.zip"
    hash = "cba78f437b9628c216a4ae0487fbb30e15d9c4b235aa55d9a0d4742fdc8d11c5"
    files = [
        {
            "name": "mandl2019ger.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter and facebook"
        },
    ]
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        file1 = helpers.clean_csv(os.path.join(tmp_file_path, "german_dataset/german_dataset.tsv"), sep='\t')
        file2 = helpers.clean_csv(os.path.join(tmp_file_path, "german_dataset/hasoc_de_test_gold.tsv"), sep='\t')
        
        tmp_file_path = helpers.merge_csvs({
            file1: [],
            file2: []
        })

        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "mandl2019ger.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = []
        if row["task_1"] == "NOT":
            labels.append("normal")
        elif row["task_2"] == "HATE":
            labels.append("hate")
        elif row["task_2"] == "OFFN":
            labels.append("offensive")
        elif row["task_2"] == "PRFN":
            labels.append("profane")
        
        row["labels"] = labels
        row = row.drop(["text_id","task_1","task_2"])
        return row