from . import dataset
import os
from . import helpers


class Sanguinetti2018(dataset.Dataset):
    
    name = "sanguinetti2018"
    url = "https://github.com/msang/hate-speech-corpus/raw/master/IHSC_ids.tsv"
    hash = "9c8fd7224362e5fa488ba70dbc1ae55cfc0a452d303c1508e3607e2cc2e20fa1"
    files = [
        {
            "name": "sanguinetti2018it.csv",
            "language": "it",
            "type": "training",
            "platform": "twitter"
        }
    ]
    comment = """"""
    license = """If you use the resource, please cite:

@InProceedings{SanguinettiEtAlLREC2018,
  author    = {Manuela Sanguinetti and Fabio Poletto and Cristina Bosco and Viviana Patti and Marco Stranisci},
  title     = {An Italian Twitter Corpus of Hate Speech against Immigrants},
  booktitle = {Proceedings of the 11th Conference on Language Resources and Evaluation (LREC2018), May 2018, Miyazaki, Japan},
  month     = {},
  year      = {2018},
  address   = {},
  publisher = {},
  pages     = {2798--2895},
  url       = {}
}
"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, sep="\t")
        tmp_file_path = helpers.download_tweets_for_csv(tmp_file_path, "tweet_id", api_config)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "sanguinetti2018it.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = []
        if row["hs"] == "yes":
            labels.append("hate")
        if row["aggressiveness"] != "no":
            labels.append(row["aggressiveness"] + "_aggressiveness")
        if row["offensiveness"] != "no":
            labels.append(row["aggressiveness"] + "_offensiveness")
        if row["irony"] == "yes":
            labels.append("irony")
        if row["stereotype"] == "yes":
            labels.append("stereotype")
        row["labels"] = labels
        row = row.drop(["aggressiveness","hs","irony","offensiveness","stereotype"])
        return row