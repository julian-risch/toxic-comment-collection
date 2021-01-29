from . import dataset
from . import helpers
import os

class Ahsd_en(dataset.Dataset):
    
    name = "ahsd_en"
    url = "https://github.com/t-davidson/hate-speech-and-offensive-language/raw/master/data/labeled_data.csv"
    training_files = ["ahsd_en.csv"]
    test_files = []
    license = """ """

    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, cls.name + ".csv"))