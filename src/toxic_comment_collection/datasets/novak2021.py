from . import dataset
from . import helpers
import os


class Novak2021(dataset.Dataset):
    
    name = "novak2021"
    url = "https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1398/IMSyPP_SI_anotacije_training-clarin.csv?sequence=6&isAllowed=y"
    hash = "fd6b85fa783afee7b6a61c99eb2eb16d59edda75af8b7df9a1f9ab4f2f59e458"
    files = [
        {
            "name": "novak2021sl.csv",
            "language": "gr",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """UNKNOWN"""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.download_tweets_for_csv(tmp_file_path, "ID", api_config)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "novak2021sl.csv"))

    @classmethod
    def unify_row(cls, row):
        row["labels"] = [str(row["vrsta"])]
        row = row.drop(["vrsta","tarča","annotator"])
        return row