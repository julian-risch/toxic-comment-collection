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
    license = """ """

    @classmethod
    def repair_json_file(cls, file):
        new_file = os.path.join(os.path.dirname(file), os.path.basename(file) + ".new")
        with open(file, 'r') as of:
            with open(new_file, 'w') as nf:
                nf.write("[\n")
                lines = of.readlines()
                for idx, line in enumerate(lines):
                    new_line = line
                    if idx < len(lines) -1:
                        new_line = line.replace("}\n", "},\n")
                    nf.write(new_line)
                nf.write("]\n")
        return new_file
                    

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, temp_folder):
        tmp_file_path = cls.repair_json_file(tmp_file_path)
        tmp_file_path = helpers.convert_json_to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "gao2018en.csv"))