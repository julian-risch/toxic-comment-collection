from abc import ABC, abstractmethod
import shutil
import os
from urllib.request import urlopen

from . import hate_speech_mlma

def get_datasets():
    return [
        hate_speech_mlma.Hate_speech_mlma
    ]

class Dataset(ABC):

    @staticmethod
    @property
    @abstractmethod
    def name():
        pass

    @staticmethod
    @property
    @abstractmethod
    def url():
        pass

    @staticmethod
    @property
    def license():
        return []

    @staticmethod
    @property
    def training_files():
        return []

    @staticmethod
    @property
    def test_files():
        return []

    # Downloads the dataset and saves it as CSV files
    # Uses the process method
    @classmethod
    def fetch_files(cls, dataset_folder):
        with urlopen(cls.url) as response:
            cls.process_downloaded_file(response, dataset_folder)

    # Process the downloaded file
    @classmethod
    def process_downloaded_file(cls, file_obj, destination_folder):
        file_path = os.path.join(destination_folder, cls.name + ".csv")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            shutil.copyfileobj(file_obj, f)
