from . import dataset
from . import helpers
import os

class Fox_news_user_comments_en(dataset.Dataset):
    
    name = "fox_news_user_comments_en"
    url = "https://github.com/sjtuprog/fox-news-comments/raw/master/full-comments-u.json"
    training_files = []
    test_files = []
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
    def download_and_process(cls, dataset_folder, temp_folder):
        tmp_file_path = helpers.download_from(cls.url, temp_folder)
        tmp_file_path = Fox_news_user_comments_en.repair_json_file(tmp_file_path)
        tmp_file_path = helpers.convert_json_to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, cls.name + ".csv"))