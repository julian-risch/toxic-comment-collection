from . import dataset
import os
from . import helpers

class Abusive_lang_twitter_ar(dataset.Dataset):
    
    name = "Abusive_lang_twitter_ar"
    url = "http://alt.qcri.org/~hmubarak/offensive/TweetClassification-Summary.xlsx"
    training_files = [
        "tweet_classification.csv"
        ]
    test_files = []
    license = """UNKNOWN"""

    
    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        tmp_file_path = helpers.convert_excel_to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, cls.name + ".csv"))