from . import dataset
from . import helpers
import os


class Wiegand2018(dataset.Dataset):
    
    name = "wiegand2018"
    url = "https://github.com/uds-lsv/GermEval-2018-Data/raw/master/germeval2018.test.txt"
    hash = "45f31510b305d080a933d4087b8d34f7a5e4087141718955b90357ca730074f2"
    files = [
        {
            "name": "wiegand2018de.csv",
            "language": "de",
            "type": "training",
            "platform": "twitter"
        }
    ]
    license = """lf you publish any work using the GermEval-2018 data, please cite the following publication:

Michael Wiegand, Melanie Siegel, and Josef Ruppenhofer: "Overview of the GermEval 2018 Shared Task on the Identification of Offensive Language", in Proceedings of the GermEval, 2018, Vienna, Austria."""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, api_config):
        tmp_file_path = helpers.clean_csv(tmp_file_path, names=["text", "tag1", "tag2"], sep='\t')
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "wiegand2018de.csv"))

    @classmethod
    def unify_row(cls, row):
        labels = [row["tag1"], row["tag2"]]
        row["labels"] = labels
        row = row.drop(["tag1","tag2"])
        return row