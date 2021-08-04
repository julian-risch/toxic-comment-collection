from . import dataset
import os
from . import helpers


class Ibrohim2019(dataset.Dataset):
    
    name = "ibrohim2019"
    url = "https://github.com/okkyibrohim/id-multi-label-hate-speech-and-abusive-language-detection/raw/master/re_dataset.csv"
    hash = "44c04e31ad4b7ee4a95f1884e7af4da2c44b69762143eb2de0ede7f90502735e"
    files = [
        {
            "name": "ibrohim2019id.csv",
            "language": "id",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """HS : hate speech label;
Abusive : abusive language label;
HS_Individual : hate speech targeted to an individual;
HS_Group : hate speech targeted to a group;
HS_Religion : hate speech related to religion/creed;
HS_Race : hate speech related to race/ethnicity;
HS_Physical : hate speech related to physical/disability;
HS_Gender : hate speech related to gender/sexual orientation;
HS_Gender : hate related to other invective/slander;
HS_Weak : weak hate speech;
HS_Moderate : moderate hate speech;
HS_Strong : strong hate speech.
"""
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "ibrohim2019id.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["Tweet"]

        labels = []
        for label in ["HS","Abusive","HS_Individual","HS_Group","HS_Religion","HS_Race","HS_Physical","HS_Gender","HS_Other","HS_Weak","HS_Moderate","HS_Strong"]:
            if row[label] == 1:
                labels.append(label)
        
        row["labels"] = labels
        row = row.drop(["Tweet","HS","Abusive","HS_Individual","HS_Group","HS_Religion","HS_Race","HS_Physical","HS_Gender","HS_Other","HS_Weak","HS_Moderate","HS_Strong"])
        return row