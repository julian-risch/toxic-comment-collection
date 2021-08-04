from . import dataset
from . import helpers
import os


class Pitenis2020(dataset.Dataset):
    
    name = "pitenis2020"
    url = "https://zpitenis.com/downloads/offenseval2020-greek.zip"
    hash = "4b1cbbcf1795b078d57640144b6cd72686b6e326dcc65e801799680f3a47bbb1"
    files = [
        {
            "name": "pitenis2020gr.csv",
            "language": "gr",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        extracted_file_path = helpers.unzip_file(tmp_file_path)
        file1 = helpers.clean_csv(os.path.join(extracted_file_path, "offenseval-gr-testsetv1/offenseval-gr-labela-v1.csv"), names=["lid", "category"])
        file2 = helpers.clean_csv(os.path.join(extracted_file_path, "offenseval-gr-testsetv1/offenseval-gr-test-v1.tsv"), names=["rid", "tweet"], sep="\t", header=0)
        tmp_file_path = helpers.join_csvs(file1, "lid", file2, "rid")
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "pitenis2020gr.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["tweet"]
        row["labels"] = [row["category"]]
        row = row.drop(["lid", "rid", "tweet", "category"])
        return row