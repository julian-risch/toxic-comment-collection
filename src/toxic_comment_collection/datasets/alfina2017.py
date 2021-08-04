from . import dataset
import os
from . import helpers

class Alfina2017(dataset.Dataset):
    
    name = "alfina2017"
    url = "https://github.com/ialfina/id-hatespeech-detection/raw/master/IDHSD_RIO_unbalanced_713_2017.txt"
    hash = "4ee1d9cc1f1fdd27fb4298207fabb717f4e09281bd68fa5dcbcf720d75f1d4ed"
    files = [
        {
            "name": "alfina2017id.csv",
            "language": "id",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """ """
    license = """The dataset may be used freely, but if you want to publish paper/publication using the dataset, please cite this publication:
Ika Alfina, Rio Mulia, Mohamad Ivan Fanany, and Yudo Ekanata, "Hate Speech Detection in Indonesian Language: A Dataset and Preliminary Study ", in Proceeding of 9th International Conference on Advanced Computer Science and Information Systems 2017(ICACSIS 2017). """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, sep="\t")
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "alfina2017id.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["Tweet"]

        labels = []
        labels.append(row["Label"])
        
        row["labels"] = labels
        row = row.drop(["Label","Tweet"])
        return row