from abc import ABC, abstractmethod
from hashlib import sha256
from typing import Dict, Optional

from . import helpers
import pandas as pd
import os
import csv
import json
import ast

class Dataset(ABC):

    @staticmethod
    @property
    @abstractmethod
    def name():
        """ Name of the dataset """
        pass

    @staticmethod
    @property
    @abstractmethod
    def url():
        """ URL of the downloadable file """
        pass

    @staticmethod
    @property
    def license():
        """ License information of the dataset """
        return []

    @staticmethod
    @property
    def hash():
        """ SHA256 hash of the downloaded file """
        return ""

    @staticmethod
    @property
    def files():
        """ List of dicts for each file that will be created during processing.
        
            Each dict should contain the following information:
            name -- the file name
            language -- ISO 639-1 code of the language
            type -- training or test
            platform -- platfrom of the generated data (e.g. twitter, facebook,...)"""
        return []

    @classmethod
    def download(cls, file_name : str):
        """ Download a file from cls.url
        
            Keyword arguments:
            file_name -- file_path where the downloaded file will be stored (including file name)
        """
        return helpers.download_from(cls.url, file_name)

    @classmethod
    @abstractmethod
    def process(cls, tmp_file_path : str, dataset_folder : str, api_config : Optional[Dict] = None):
        """ Process the downloaded file. The processed file should be copied to the corresponding dataset_folder in this method.
        
            Keyword arguments:
            tmp_file_path -- path of the file to process
            dataset_folder -- path where the resulting file should be stored
        """
        pass

    @classmethod
    def valid_hash(cls, file : str):
        """ Calculate the SHA256 hash of the given file and print a warning if the hash differs.
        
            Keyword arguments:
            file -- path of the file to hash
        """
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
            print("WARNING: " + cls.name + ": Expected Dataset hash to be " + cls.hash + " but was " + hash_value)
            return False

    @classmethod
    def unify_row(cls, row : pd.Series):
        """ This method is called for each row in the dataset. Use this method to filter attributes and rename columns.
        
            Keyword arguments:
            row -- pandas.Series that contains the row
        """
        return row

    @classmethod
    def translate_row(cls, row : pd.Series, translation : dict):
        """ This method is called for each row in the dataset. Translate the labels according to config.json.
        
            Keyword arguments:
            row -- pandas.Series that contains the row
            translation -- dict that contains the translations
        """
        translated_labels = []
        if type(row["labels"]) == str:
            row["labels"] = ast.literal_eval(row["labels"])
        for i in row["labels"]:
            translated_labels.extend(translation.get(i, [i]))
        row["labels"] = list(set(translated_labels))
        return row

    @classmethod
    def unify(cls, config : Dict, dataset_name : str):
        """ Perform unification of the dataset files
        
            Keyword arguments:
            config -- supplied config
            dataset_name -- name of the dataset to be unified
        """
        dataset_folder = os.path.join(config["file_directory"], dataset_name)
        for file in cls.files:
            df = pd.read_csv(os.path.join(dataset_folder, file["name"]))
            df = cls.unify_format(df)
            if (config and file["name"] in config["datasets"]):
                df = cls.translate_labels(df, config["datasets"][file["name"]]["translation"])
            df.to_csv(os.path.join(dataset_folder, file["name"]), index_label="id", quoting=csv.QUOTE_NONNUMERIC, sep="\t")

    @classmethod
    def translate_labels(cls, df : pd.DataFrame, translation : dict):
        """ Perform label translation of the dataset file
        
            Keyword arguments:
            df -- pandas.DataFrame that contains the data
            translation -- dict that contains the translations
        """
        return df.apply(cls.translate_row, axis=1, args=(translation,))

    @classmethod
    def unify_format(cls, df : pd.DataFrame):
        """ Calls the unfiy method for each entry of the dataset
        
            Keyword arguments:
            df -- pandas.DataFrame that contains the dataset data
        """
        return df.apply(cls.unify_row, axis=1) 