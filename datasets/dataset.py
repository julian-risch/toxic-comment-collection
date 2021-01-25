from abc import ABC, abstractmethod

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

    # This method should assure, that the dataset is downloaded and processed, so that the CSV files are present in the given destination folder
    @classmethod
    def download_and_process(cls, dataset_folder, temp_folder):
        pass