from . import dataset
import os
from . import helpers


class Coltekin2019(dataset.Dataset):
    
    name = "coltekin2019"
    url = "https://coltekin.github.io/offensive-turkish/offenseval2020-turkish.zip"
    hash = "7977e96255dbc9b8d14893f1b14cbe3dec53c70358503c062c5a59720ec9c2f2"
    files = [
        {
            "name": "coltekin2019tr.csv",
            "language": "tr",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """ """
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        zip_file_path = helpers.unzip_file(tmp_file_path)
        file1 = os.path.join(zip_file_path, "offenseval2020-turkish/offenseval-tr-testset-v1/offenseval-tr-labela-v1.tsv")
        file1 = helpers.clean_csv(file1, sep=",", names=["lid", "class"])
        file2 = os.path.join(zip_file_path, "offenseval2020-turkish/offenseval-tr-testset-v1/offenseval-tr-testset-v1.tsv")
        file2 = helpers.clean_csv(file2, sep="\t", names=["rid", "text"], header=0)
        tmp_file_path = helpers.join_csvs(file1, "lid", file2, "rid")
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "coltekin2019tr.csv"))

    @classmethod
    def unify_row(cls, row):
        row["labels"] = [row["class"]]
        row = row.drop(["lid", "rid", "class"])
        return row