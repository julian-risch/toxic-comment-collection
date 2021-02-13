from . import dataset
import os
import zipfile
from io import BytesIO
from . import helpers

class Ousidhoum2019(dataset.Dataset):
    
    name = "ousidhoum2019"
    url = "https://github.com/HKUST-KnowComp/MLMA_hate_speech/raw/master/hate_speech_mlma.zip"
    hash = "56db7efb1b64a2570f63d0cdb48d119c5e32eccff13f3c22bf17a4331956dc43"
    files = [
        {
            "name": "ousidhoum2019ar.csv",
            "language": "ar",
            "type": "training",
            "platform": "twitter"
        },
        {
            "name": "ousidhoum2019en_with_stopwords.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        },
        {
            "name": "ousidhoum2019en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        },
        {
            "name": "ousidhoum2019fr.csv",
            "language": "fr",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """MIT License

Copyright (c) 2019 HKUST-KnowComp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

    @classmethod
    def download(cls, temp_folder):
        return helpers.download_from(cls.url, temp_folder)

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, temp_folder):
        tmp_dir_path = helpers.unzip_file(tmp_file_path)
        helpers.copy_file(os.path.join(tmp_dir_path, "hate_speech_mlma/ar_dataset.csv"), os.path.join(dataset_folder, "ousidhoum2019ar.csv"))
        helpers.copy_file(os.path.join(tmp_dir_path, "hate_speech_mlma/en_dataset.csv"), os.path.join(dataset_folder, "ousidhoum2019en.csv"))
        helpers.copy_file(os.path.join(tmp_dir_path, "hate_speech_mlma/fr_dataset.csv"), os.path.join(dataset_folder, "ousidhoum2019fr.csv"))
        helpers.copy_file(os.path.join(tmp_dir_path, "hate_speech_mlma/en_dataset_with_stop_words.csv"), os.path.join(dataset_folder, "ousidhoum2019en_with_stopwords.csv"))
        