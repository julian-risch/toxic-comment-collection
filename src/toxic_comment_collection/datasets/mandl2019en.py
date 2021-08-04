from . import dataset
from . import helpers
import os


class Mandl2019en(dataset.Dataset):
    
    name = "mandl2019en"
    url = "https://hasocfire.github.io/hasoc/2019/files/english_dataset.zip"
    hash = "1b4bda7904193be59ed768675fc1d65f172f7bf92af3de6394e8deda8afb640e"
    files = [
        {
            "name": "mandl2019en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter and facebook"
        },
    ]
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        file1 = helpers.clean_csv(os.path.join(tmp_file_path, "english_dataset/english_dataset.tsv"), sep='\t')
        file2 = helpers.clean_csv(os.path.join(tmp_file_path, "english_dataset/hasoc2019_en_test-2919.tsv"), sep='\t')
        
        tmp_file_path = helpers.merge_csvs({
            file1: [],
            file2: []
        })

        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "mandl2019en.csv"))

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
        
        if row["task_3"] == "TIN":
            labels.append("targeted")
        elif row["task_3"] == "UNT":
            labels.append("untargeted")
        
        row["labels"] = labels
        row = row.drop(["text_id","task_1","task_2","task_3"])
        return row