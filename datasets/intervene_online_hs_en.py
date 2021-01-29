from . import dataset
from . import helpers
import os

class Intervene_online_hs_en(dataset.Dataset):
    
    name = "intervene_online_hs_en"
    url = "https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech/archive/master.zip"
    training_files = []
    test_files = []
    license = """ """

    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        helpers.copy_file(os.path.join(tmp_file_path, "A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech-master/data/gab.csv"), os.path.join(dataset_folder, cls.name + "1.csv"))
        helpers.copy_file(os.path.join(tmp_file_path, "A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech-master/data/reddit.csv"), os.path.join(dataset_folder, cls.name + "2.csv"))