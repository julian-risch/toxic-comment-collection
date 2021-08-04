from . import dataset
from . import helpers
import os

class Davidson2017(dataset.Dataset):
    
    name = "davidson2017"
    url = "https://github.com/t-davidson/hate-speech-and-offensive-language/raw/master/data/labeled_data.csv"
    hash = "fcb8bc7c68120ae4af04a5b9acd58585513ede11e1548ebf36a5c2040b6f6281"
    files = [
        {
            "name": "davidson2017en.csv",
            "language": "en",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """MIT License

Copyright (c) 2017 Tom Davidson

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
    def process(cls, tmp_file_path, dataset_folder, api_config):
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "davidson2017en.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["tweet"]
        labels = []
        if row["class"] == 0:
            labels.append("hate")
        if row["class"] == 1:
            labels.append("offensive")
        if row["class"] == 2:
            labels.append("normal")
        row["labels"] = labels
        row = row.drop(["Unnamed: 0","count","hate_speech","offensive_language","neither","class", "tweet"])
        return row
        