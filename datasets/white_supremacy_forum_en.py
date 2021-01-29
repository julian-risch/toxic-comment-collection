from . import dataset
from . import helpers
import pandas as pd
import os

class White_supremacy_forum_en(dataset.Dataset):
    
    name = "white_supremacy_forum_en"
    url = "https://github.com/Vicomtech/hate-speech-dataset/archive/master.zip"
    training_files = []
    test_files = []
    license = """The resources in this repository are licensed under the Creative Commons Attribution-ShareAlike 3.0 Spain
License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/es/ or send
a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA."""

    @classmethod
    def replace_csv_entry_with_filecontents(cls, row, directory):
        fid = row["file_id"]
        with open(os.path.join(directory, "all_files", fid + ".txt"), 'r') as f:
            row["text"] = "\n".join(f.readlines())
            return row

    @classmethod
    def merge_txt_to_csv(cls, directory):
        df = pd.read_csv(os.path.join(directory, "annotations_metadata.csv"))
        df = df.apply(White_supremacy_forum_en.replace_csv_entry_with_filecontents, axis=1, args=(directory,))
        output_file = os.path.join(directory, cls.name + ".csv")
        df.to_csv(output_file)
        return output_file

    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        extraction_dir = helpers.unzip_file(tmp_file_path)
        tmp_file_path = White_supremacy_forum_en.merge_txt_to_csv(os.path.join(extraction_dir, "hate-speech-dataset-master"))
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, cls.name + ".csv"))