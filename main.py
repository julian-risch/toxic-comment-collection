import datasets
from datasets import hate_speech_mlma
import os
import shutil

TEMPDIR = "./tmp"
FILEDIR = "./files"

def fetch_datasets():
    clear_all()
    for idx, dataset in enumerate(datasets.get_datasets()):
        clear_directory(TEMPDIR)
        dataset.download_and_process(os.path.join(FILEDIR, str(idx)), TEMPDIR)

def clear_all():
    clear_directory(TEMPDIR)
    clear_directory(FILEDIR)
    
def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)

if __name__ == '__main__':
    fetch_datasets()
