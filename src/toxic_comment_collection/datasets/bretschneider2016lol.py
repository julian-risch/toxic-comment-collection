from . import dataset
import os
from . import helpers

class Bretschneider2016lol(dataset.Dataset):
    
    name = "bretschneider2016lol"
    url = "http://ub-web.de/research/resources/lol_anonymized.zip"
    hash = "901e0d51428f34b94bf6b3f59b0e9cf71dabe94fc74fd81fd1e9be199d2902bc"
    files = [
        {
            "name": "bretschneider2016en_lol.csv",
            "language": "en",
            "type": "training",
            "platform": "League of Legends"
        }
    ]
    comment = """ """
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        tmp_file_path = helpers.extract_sql_tables(os.path.join(tmp_file_path, "lol_anonymized.sql"))
        tmp_file_path = helpers.join_csvs(os.path.join(tmp_file_path, "posts.csv"), ["topic_id", "post_number"], os.path.join(tmp_file_path, "annotations.csv"), ["topic_id", "post_number"], how='left')
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "bretschneider2016en_lol.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["html_message"]
        labels = []
        if (type(row["offender"]) != float):        # contains NaN when join didn't happen, which is a float
            labels.append("offensive")

        row["labels"] = labels
        row = row.drop(["topic_id","post_number","annotator","offender","victim","author","html_message","timestamp"])
        return row
