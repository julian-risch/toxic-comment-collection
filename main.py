import datasets
import os
import shutil
import sys
import getopt
import statistics_generator
import json
import csv
import datasets.helpers as helpers
import pandas as pd

config = {}

def main(args):

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except:
        print("Failure loading config.json. Run the following command to reset config.json:\n\n\tmain.py --genconfig")
        exit()

    try:
        arguments = dict(getopt.getopt(args, "-r -? -s -g -c -d", [
                         'reset', 'help', 'statistics', 'genconfig', 'skipCombine', 'skipDownload'])[0])
    except:
        print("Invalid argument!\n")
        print_help()
        return -1

    if ("--statistics" in arguments or "-s" in arguments):
        generate_statistics(config["file_directory"])
        exit()

    if ("--genconfig" in arguments or "-g" in arguments):
        generate_config(config["file_directory"])
        exit()

    if ("--help" in arguments or "-?" in arguments):
        print_help()
        exit()

    if ("--reset" in arguments or "-r" in arguments):
        clear_all(config)
        exit()

    if not ("--skipDownload" in arguments or "-d" in arguments):
        max_suffix_length = download_datasets(config)
        max_suffix_length = process_datasets(config, max_suffix_length)
    else:
        max_suffix_length = 0

    max_suffix_length = unify_datasets(config, max_suffix_length)

    if not ("--skipCombine" in arguments or "-c" in arguments):
        combine_datasets(config["file_directory"])


def print_help():
    print("""Usage: python3 main.py [-r][-?]
    
-r  --reset         Reset all existing files, deletes everything in folders 'tmp' and 'files'

-?  --help          Show this help

-d  --skipDownload  Do not re-download the datasets (does not included hydrating twitter data)

-u  --skipUnify     Do not perform label translation as configured in config.json

-c  --skipCombine   Do not combine all datasets into combined.tsv

-g  --genconfig     Generate or Update the config file

-s  --statistcs     Generates statistics about the downloaded datasets. Make sure to run
                    the script without the -s parameter before to download the datasets.
                    Does not work with unprocessed data (-o)""")


def combine_datasets(filedir, output_file_name="combined.tsv"):
    output_file = os.path.join(filedir, output_file_name)
    combined_df = pd.DataFrame()
    for dataset in datasets.get_datasets():
        for ds_file in dataset.files:
            df = pd.read_csv(os.path.join(
                filedir, dataset.name, ds_file["name"]), sep="\t")
            df.insert(loc=0, column="file_name", value=[
                      ds_file["name"]] * df.count().max())
            df.insert(loc=0, column="file_language", value=[
                      ds_file["language"]] * df.count().max())
            df.insert(loc=0, column="file_platform", value=[
                      ds_file["platform"]] * df.count().max())
            df.drop(columns=["id"], inplace=True)
            combined_df = combined_df.append(df)
    combined_df.to_csv(output_file, index_label="id",
                       quoting=csv.QUOTE_NONNUMERIC, sep="\t")

def unify_datasets(config, max_suffix_length=0):
    _clear_directory(config["file_directory"])

    for idx, dataset in enumerate(datasets.get_datasets()):
        max_suffix_length = _print_progress_bar(idx + len(datasets.get_datasets()) *2, len(datasets.get_datasets()) * 3, "Unify " + dataset.name, max_suffix_length)
        
        for ds_file in dataset.files:
            helpers.copy_file(os.path.join(config["raw_directory"], dataset.name + "_dir", ds_file["name"]), os.path.join(config["file_directory"], dataset.name, ds_file["name"]))
        
        dataset.unify(os.path.join(config["file_directory"], dataset.name))


    _print_progress_bar(len(datasets.get_datasets()) *3, len(datasets.get_datasets()) *3, "Done", max_suffix_length)
    return max_suffix_length

def process_datasets(config, max_suffix_length=0):
    for idx, dataset in enumerate(datasets.get_datasets()):
        max_suffix_length = _print_progress_bar(
            idx + len(datasets.get_datasets()), len(datasets.get_datasets()) * 3, "Process " + dataset.name, max_suffix_length)

        _clear_directory(config["temp_directory"])
        tmp_file_name = os.path.join(config["temp_directory"], dataset.name)
        helpers.copy_file(os.path.join(config["raw_directory"], dataset.name), tmp_file_name)
        
        dataset.process(tmp_file_name, os.path.join(config["raw_directory"], dataset.name + "_dir"))
    
    return max_suffix_length

def download_datasets(config, max_suffix_length=0) -> int:
    _clear_directory(config["raw_directory"])

    for idx, dataset in enumerate(datasets.get_datasets()):
        max_suffix_length = _print_progress_bar(
            idx, len(datasets.get_datasets()) * 3, "Download " + dataset.name, max_suffix_length)

        if config["data_sources"].get(dataset.name, True):
            file = dataset.download(os.path.join(config["raw_directory"], dataset.name))
            dataset.valid_hash(file)

    return max_suffix_length
        
def generate_statistics(filedir):
    sg = statistics_generator.Statistics_generator(filedir)
    sg.generate("statistics.txt")


def generate_config(filedir):
    if (not os.path.isfile("api_config.json") or input("Reset api_config.json completely? [y/n] ") == "y"):
        with open("api_config.json", "w") as f:
            json.dump(
                {"twitter" : {
                    "consumer_key": "",
                    "consumer_secret": "",
                    "access_token": "",
                    "access_token_secret": "",
                    }
                }, f)

    if (os.path.isfile("config.json") and input("Reset config.json completely? [y/n] ") != "y"):
        with open("config.json", "r") as f:
            config = json.load(f)
    else:
        print("Generating new config.json")
        config = {}

    if (not "temp_directory" in config):
        config["temp_directory"] = "./tmp"

    if (not "file_directory" in config):
        config["file_directory"] = "./files"

    if (not "raw_directory" in config):
        config["raw_directory"] = "./raw"

    if (not "data_sources" in config or input("Reset Datasources? [y/n] ") == "y"):
        config["data_sources"] = {}

    for dataset in datasets.get_datasets():
        config["data_sources"][dataset.name] = { "download": True } 

    if (not "datasets" in config or input("Reset Dataset Config? [y/n] ") == "y"):
        config["datasets"] = {}

    ds_data, _ = statistics_generator.Statistics_generator(filedir).generate()

    for ds in ds_data:
        translation_table = {}
        for label in ds_data[ds]["labels"]:
            translation_table[label] = [label]
        if not ds in config["datasets"]:
            config["datasets"][ds] = {
                "translation": translation_table, "download": True}
        else:
            if "translation" in config["datasets"][ds]:
                for i in config["datasets"][ds]["translation"]:
                    if (not i in translation_table.values()):
                        translation_table[i] = config["datasets"][ds]["translation"][i]
            config["datasets"][ds]["translation"] = translation_table

    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)


def clear_all(config):
    _clear_directory(config["file_directory"])
    _clear_directory(config["temp_directory"])
    _clear_directory(config["raw_directory"])


def _clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)

def _print_progress_bar(iteration, total, suffix='', max_suffix_length=0):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(50 * iteration // total)
    bar = '█' * filledLength + '-' * (50 - filledLength)
    suffix_string = suffix + (' ' * (max_suffix_length - len(suffix)))
    print(f'\rProgress: [{bar}] {percent}% {suffix_string}', end='\r')
    if iteration == total:
        print()
    return len(suffix_string)


if __name__ == '__main__':
    main(sys.argv[1:])
