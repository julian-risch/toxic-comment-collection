from . import dataset
import os
import pandas as pd
from io import BytesIO

class Abusive_lang_aljazeera_ar(dataset.Dataset):
    
    name = "abusive_lang_aljazeera_ar"
    url = "http://alt.qcri.org/~hmubarak/offensive/AJCommentsClassification-CF.xlsx"
    training_files = []
    test_files = []
    license = """ """

    @classmethod
    def process_downloaded_file(cls, file_obj, destination_folder):
        file_path = os.path.join(destination_folder, cls.name + ".csv")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        excel_file = pd.read_excel(BytesIO(file_obj.read()))
        with open(file_path, 'wb') as f:
            excel_file.to_csv(f)