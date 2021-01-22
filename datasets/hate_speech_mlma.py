from . import dataset
import os
import zipfile
from io import BytesIO

class Hate_speech_mlma(dataset.Dataset):
    
    name = "MLMA_hate_speech"
    url = "https://github.com/HKUST-KnowComp/MLMA_hate_speech/raw/master/hate_speech_mlma.zip"
    training_files = [
        "ar_dataset.csv",
        "en_dataset_with_stop_words.csv",
        "en_dataset.csv",
        "fr_dataset.csv"
        ]
    test_files = []
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
    def process_downloaded_file(cls, file_obj, destination_folder):
        os.makedirs(destination_folder, exist_ok=True)
        with zipfile.ZipFile(BytesIO(file_obj.read())) as zip_file:
            zip_file.extractall(destination_folder)