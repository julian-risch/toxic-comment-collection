from . import dataset
from . import helpers
import os

class Davidson2017(dataset.Dataset):
    
    name = "davidson2017"
    url = "https://github.com/t-davidson/hate-speech-and-offensive-language/raw/master/data/labeled_data.csv"
    hash = "fcb8bc7c68120ae4af04a5b9acd58585513ede11e1548ebf36a5c2040b6f6281"
    files = [
        {
            "name": "davidson2017en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, temp_folder):
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "davidson2017en.csv"))