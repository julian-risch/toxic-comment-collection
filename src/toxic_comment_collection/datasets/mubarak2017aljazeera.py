import os
from . import dataset
from . import helpers

class Mubarak2017aljazeera(dataset.Dataset):
    
    name = "mubarak2017aljazeera"
    url = "http://alt.qcri.org/~hmubarak/offensive/AJCommentsClassification-CF.xlsx"
    hash = "afa00e36ff5492c1bbdd42a0e4979886f40d00f1aa5517807a957e22fb517670"
    files = [
        {
            "name": "mubarak2017ar_aljazeera.csv",
            "language": "ar",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """Annotation	Meaning
0	NORMAL_LANGUAGE
-1	OFFENSIVE_LANGUAGE
-2	OBSCENE_LANGUAGE"""
    license = """ """

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.convert_excel_to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "mubarak2017ar_aljazeera.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["body"]
        labels = []
        if row["languagecomment"] == 0:
            labels.append("normal")
        if row["languagecomment"] == -1:
            labels.append("offensive")
        if row["languagecomment"] == -2:
            labels.append("obscene")
        row["labels"] = labels
        row = row.drop(["_unit_id","_golden","_unit_state","_trusted_judgments","_last_judgment_at","languagecomment","languagecomment:confidence","articletitle","body","bodylen","insdt","languagecomment_gold","link","serial","words"])
        return row