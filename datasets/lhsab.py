from . import dataset
from . import helpers
import os

class Lhsab(dataset.Dataset):
    
    name = "l-hsab"
    url = "https://github.com/Hala-Mulki/L-HSAB-First-Arabic-Levantine-HateSpeech-Dataset/raw/master/Dataset/L-HSAB"
    training_files = [
        "l-hsab.csv"
        ]
    test_files = []
    license = """UNKNOWN"""

    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, cls.name + ".csv"))