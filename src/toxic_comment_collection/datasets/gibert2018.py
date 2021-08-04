from . import dataset
from . import helpers
import pandas as pd
import os

class Gibert2018(dataset.Dataset):
    
    name = "gibert2018"
    url = "https://github.com/Vicomtech/hate-speech-dataset/archive/master.zip"
    hash = "acc0d7ce40e22cf019daa752a5136049a45462b9ba4eab8bf40ea82dcd867eba"
    files = [
        {
            "name": "gibert2018en.csv",
            "language": "en",
            "type": "training",
            "platform": "stormfront"
        }
    ]
    license = """The resources in this repository are licensed under the Creative Commons Attribution-ShareAlike 3.0 Spain
License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/es/ or send
a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA."""

    @classmethod
    def replace_csv_entry_with_filecontents(cls, row, directory):
        fid = row["file_id"]
        with open(os.path.join(directory, "all_files", fid + ".txt"), 'r', encoding="utf-8") as f:
            row["text"] = "\n".join(f.readlines())
            return row

    @classmethod
    def merge_txt_to_csv(cls, directory):
        df = pd.read_csv(os.path.join(directory, "annotations_metadata.csv"), encoding="utf-8")
        df = df.apply(cls.replace_csv_entry_with_filecontents, axis=1, args=(directory,))
        output_file = os.path.join(directory, cls.name + ".csv")
        df.to_csv(output_file)
        return output_file

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        extraction_dir = helpers.unzip_file(tmp_file_path)
        tmp_file_path = cls.merge_txt_to_csv(os.path.join(extraction_dir, "hate-speech-dataset-master"))
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "gibert2018en.csv"))

    @classmethod
    def unify_row(cls, row):        
        row["labels"] = [row["label"]]
        row = row.drop(["Unnamed: 0","subforum_id","file_id","user_id","num_contexts","label"])
        return row