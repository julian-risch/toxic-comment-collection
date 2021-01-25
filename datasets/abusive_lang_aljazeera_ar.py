from . import dataset
import os
import pandas as pd
from io import BytesIO
from . import helpers

class Abusive_lang_aljazeera_ar(dataset.Dataset):
    
    name = "abusive_lang_aljazeera_ar"
    url = "http://alt.qcri.org/~hmubarak/offensive/AJCommentsClassification-CF.xlsx"
    training_files = []
    test_files = []
    license = """ """

    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        tmp_file_path = helpers.convert_excel_to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, cls.name + ".csv"))