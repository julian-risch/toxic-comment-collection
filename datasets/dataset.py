from abc import ABC, abstractmethod
from hashlib import sha256
from . import helpers

import logging

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
    def hash():
        return ""

    @staticmethod
    @property
    def files():
        return []

    @classmethod
    def download(cls, temp_folder):
        return helpers.download_from(cls.url, temp_folder)

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, temp_folder):
        pass

    @classmethod
    def valid_hash(cls, file):
        hash = sha256()

        with open(file, 'rb') as file:
            while True:
                chunk = file.read(hash.block_size)
                if not chunk:
                    break
                hash.update(chunk)
        hash_value = hash.hexdigest()
        if cls.hash == hash_value:
            return True
        else:
            logging.warning(cls.name + ": Expected Dataset hash to be " + cls.hash + " but was " + hash_value)
            return False
        