from . import dataset
from . import helpers
import os
import json
import pandas as pd

class Conan(dataset.Dataset):
    
    name = "conan"
    url = "https://github.com/marcoguerini/CONAN/raw/master/CONAN.json"
    training_files = []
    test_files = []
    license = """ """

    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        with open(tmp_file_path, "r") as f:
            a = json.load(f)
        b = pd.DataFrame(a['conan'])
        tmp_file_path = tmp_file_path + ".csv"
        b.to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, cls.name + ".csv"))