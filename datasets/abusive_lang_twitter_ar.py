from . import dataset
import os
from io import BytesIO
import pandas as pd

class Abusive_lang_twitter_ar(dataset.Dataset):
    
    name = "Abusive_lang_twitter_ar"
    url = "http://alt.qcri.org/~hmubarak/offensive/TweetClassification-Summary.xlsx"
    training_files = [
        "tweet_classification.csv"
        ]
    test_files = []
    license = """UNKNOWN"""

    
    @classmethod
    def process_downloaded_file(cls, file_obj, destination_folder):
        file_path = os.path.join(destination_folder, cls.name + ".csv")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        excel_file = pd.read_excel(BytesIO(file_obj.read()))
        with open(file_path, 'wb') as f:
            excel_file.to_csv(f)