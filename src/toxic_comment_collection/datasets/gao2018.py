from . import dataset
from . import helpers
import os

class Gao2018(dataset.Dataset):
    
    name = "gao2018"
    url = "https://github.com/sjtuprog/fox-news-comments/raw/master/full-comments-u.json"
    hash = "059152e61f632f1e6671a68214d5618a21e6cf78f2512773e0421b9568aab8cf"
    files = [
        {
            "name": "gao2018en.csv",
            "language": "en",
            "type": "training",
            "platform": "fox news"
        }
    ]
    comment = """Inflammatory language explicitly or implicitly threatens or demeans a person or agroup based upon a facet of their identity such as gender, ethnicity, or sexualorientation.
- Excludes insults towards other anonymous users
- Includes insults of belief systems"""

    license = """The MIT License

Copyright (c) 2010-2019 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE."""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.convert_jsonl_to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "gao2018en.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = []
        if row["label"] == 0:
            labels.append("normal")
        if row["label"] == 1:
            labels.append("hate")
        row["labels"] = labels
        row = row.drop(["title","succ","meta","user","mentions","prev", "label"])
        return row