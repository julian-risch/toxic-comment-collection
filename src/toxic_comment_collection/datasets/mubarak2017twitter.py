from . import dataset
import os
from . import helpers

class Mubarak2017twitter(dataset.Dataset):
    
    name = "mubarak2017twitter"
    url = "http://alt.qcri.org/~hmubarak/offensive/TweetClassification-Summary.xlsx"
    hash = "606f73388adae60af740779f9b501f30cf9adac82afe15a46fe07155db3823cf"
    files = [
        {
            "name": "mubarak2017ar_twitter.csv",
            "language": "ar",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """Annotation	Meaning
0	NORMAL_LANGUAGE
-1	OFFENSIVE_LANGUAGE
-2	OBSCENE_LANGUAGE"""
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.convert_excel_to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "mubarak2017ar_twitter.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = []
        if row["aggregatedAnnotation"] == 0:
            labels.append("normal")
        if row["aggregatedAnnotation"] == -1:
            labels.append("offensive")
        if row["aggregatedAnnotation"] == -2:
            labels.append("obscene")
        row["labels"] = labels
        row = row.drop(["#","type","aggregatedAnnotation","aggregatedAnnotationConfidence","annotator1","annotator2","annotator3"])
        return row