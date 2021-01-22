from . import dataset

class Lhsab(dataset.Dataset):
    
    name = "l-hsab"
    url = "https://github.com/Hala-Mulki/L-HSAB-First-Arabic-Levantine-HateSpeech-Dataset/raw/master/Dataset/L-HSAB"
    training_files = [
        "l-hsab.csv"
        ]
    test_files = []
    license = """UNKNOWN"""
