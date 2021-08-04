from . import dataset
import os
from . import helpers


class Bretschneider2016wow(dataset.Dataset):
    
    name = "bretschneider2016wow"
    url = "http://www.ub-web.de/research/resources/wow_anonymized.zip"
    hash = "0f5d67879306cd67154c31583b6e8750b9290f54c0065cc8cdf11ab6a8d1a26d"
    files = [
        {
            "name": "bretschneider2016en_wow.csv",
            "language": "en",
            "type": "training",
            "platform": "World of Warcraft"
        }
    ]
    comment = """ """
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.unzip_file(tmp_file_path)
        tmp_file_path = helpers.extract_sql_tables(os.path.join(tmp_file_path, "wow_anonymized.sql"))
        tmp_file_path = helpers.join_csvs(os.path.join(tmp_file_path, "posts.csv"), ["topic_id", "post_number"], os.path.join(tmp_file_path, "annotations.csv"), ["topic_id", "post_number"], how='left')
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "bretschneider2016en_wow.csv"))

    @classmethod
    def unify_row(cls, row):
        row["text"] = row["html_message"]
        labels = []
        if (type(row["offender"]) != float):        # contains NaN when join didn't happen, which is a float
            labels.append("offensive")

        row["labels"] = labels
        row = row.drop(["topic_id","post_number","annotator","offender","victim","author","html_message","timestamp"])
        return row
