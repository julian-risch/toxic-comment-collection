from . import dataset
from . import helpers
import os

class Hate_speech_mlma(dataset.Dataset):
    
    name = ""
    url = ""
    training_files = []
    test_files = []
    license = """ """

    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, cls.name + ".csv"))