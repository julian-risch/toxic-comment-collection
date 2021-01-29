from . import dataset
from . import helpers

class OLID(dataset.Dataset):
    
    name = "olid"
    url = "https://sites.google.com/site/offensevalsharedtask/olid/OLIDv1.0.zip"
    training_files = []
    test_files = []
    license = """ """

    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)