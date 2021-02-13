from . import dataset
from . import helpers
import os

class Qian2019(dataset.Dataset):
    
    name = "qian2019"
    url = "https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech/archive/master.zip"
    hash = "e2774f61af64942373e76e3928269bf6b7d8b41d5f5dcbcac9e760d4e93ef6b4"
    files = [
        {
            "name": "chung2019en_gab.csv",
            "language": "en",
            "type": "training",
            "platform": "gab"
        },
        {
            "name": "chung2019en_reddit.csv",
            "language": "en",
            "type": "training",
            "platform": "reddit"
        }
    ]
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, temp_folder):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        helpers.copy_file(os.path.join(tmp_file_path, "A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech-master/data/gab.csv"), os.path.join(dataset_folder, "chung2019en_gab.csv"))
        helpers.copy_file(os.path.join(tmp_file_path, "A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech-master/data/reddit.csv"), os.path.join(dataset_folder, "chung2019en_reddit.csv"))