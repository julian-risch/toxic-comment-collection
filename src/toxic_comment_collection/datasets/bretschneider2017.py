from . import dataset
import os
from . import helpers


class Bretschneider2017(dataset.Dataset):
    
    name = "bretschneider2017"
    url = "http://ub-web.de/research/resources/fb_hate_speech_csv.zip"
    hash = "5d31274178d342fb6516ee1015a6ec3c8fa7076e2d6313efb43040a6f8ba26af"
    files = [
        {
            "name": "bretschneider2017en.csv",
            "language": "en",
            "type": "training",
            "platform": "facebook"
        }
    ]
    comment = """ """
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        file1 = os.path.join(tmp_file_path, "fb_hate_speech_csv/comments.csv")
        file2 = os.path.join(tmp_file_path, "fb_hate_speech_csv/annotated_comments.csv")
        tmp_file_path = helpers.join_csvs(file1, "comment_id", file2, "comment_id")
        tmp_file_path = helpers.drop_duplicates(tmp_file_path, ["comment_id"])
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "bretschneider2017en.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["message"]

        labels = []
        if row["valence"] == 1:
            labels.append("moderate")
        elif row["valence"] == 2:
            labels.append("substantially_offending")

        if row["target_type"] == 1:
            labels.append("no_target")
        elif row["target_type"] == 2:
            labels.append("targets_foreigner_refugee")
        elif row["target_type"] == 3:
            labels.append("targets_politicians_government")
        elif row["target_type"] == 5:
            labels.append("targets_other")
        elif row["target_type"] == 6:
            labels.append("targets_unknown")
        elif row["target_type"] == 7:
            labels.append("targets_page_community")
        elif row["target_type"] == 8:
            labels.append("targets_press")
        
        row["labels"] = labels
        row = row.drop(["comment_id","post_id","anonymized_user","message","created_at","annotator_id","entry_number","valence","target_type"])
        return row