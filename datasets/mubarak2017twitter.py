from . import dataset
import os
from . import helpers

class Mubarak2017twitter(dataset.Dataset):
    
    name = "mubarak2017"
    url = "http://alt.qcri.org/~hmubarak/offensive/TweetClassification-Summary.xlsx"
    hash = "606f73388adae60af740779f9b501f30cf9adac82afe15a46fe07155db3823cf"
    files = [
        {
            "name": "mubarak2017ar_twitter.csv",
            "language": "ar",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, temp_folder):
        tmp_file_path = helpers.convert_excel_to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "mubarak2017ar_twitter.csv"))