import datasets
import os
import shutil
import sys
import getopt
import statistics_generator
import json
import csv
import datasets.helpers
import pandas as pd

config = {}

def main(args):

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except:
        print("Failure loading config.json. Run the following command to reset config.json:\n\n\tmain.py --genconfig")

    try:
        arguments = dict(getopt.getopt(args, "-r -? -o -s -g -c", [
                         'reset', 'help', 'original', 'statistics', 'genconfig', 'skipCombine'])[0])
    except:
        print("Invalid argument!\n")
        print_help()
        return -1

    if ("--statistics" in arguments or "-s" in arguments):
        generate_statistics(config["file_directory"])
        exit()

    if ("--genconfig" in arguments):
        generate_config(config["file_directory"])
        exit()

    if ("--help" in arguments or "-?" in arguments):
        print_help()
        exit()

    if ("--reset" in arguments or "-r" in arguments):
        clear_all(config)
        exit()

    unify = not ("--original" in arguments or "-o" in arguments)
    fetch_datasets(config, unify_format=unify)

    if not ("--skipCombine" in arguments or "-c" in arguments):
        combine_datasets(config["file_directory"])


def print_help():
    print("""Usage: python3 main.py [-r][-?]
    
-r  --reset         Reset all existing files, deletes everything in folders 'tmp' and 'files'

-?  --help          Show this help

-o  --original      Download the datasets but don't process them

    --genconfig     Generate or Update the config file

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


def fetch_datasets(config, unify_format=True, translate_labels=True, skipDownload=False):
    filedir = config["file_directory"]
    tempdir = config["temp_directory"]
    clear_all(config)
    print("Download Data and perform initial processing")
    max_suffix_length = 0
    for idx, dataset in enumerate(datasets.get_datasets()):
        max_suffix_length = _print_progress_bar(
            idx * 2, len(datasets.get_datasets()) * 2, "Download " + dataset.name, max_suffix_length)

        _clear_directory(tempdir)
        file = dataset.download(tempdir)

        max_suffix_length = _print_progress_bar(
            idx * 2 + 1, len(datasets.get_datasets()) * 2, "Process " + dataset.name, max_suffix_length)

        dataset.valid_hash(file)
        dataset.process(file, os.path.join(filedir, dataset.name), tempdir)

        if unify_format:
            dataset.unify(os.path.join(
                filedir, dataset.name), translate_labels)
    _print_progress_bar(len(datasets.get_datasets()), len(
        datasets.get_datasets()), "Done", max_suffix_length)
    print("Done fetching Datasets")


def generate_statistics(filedir):
    sg = statistics_generator.Statistics_generator(filedir)
    sg.generate("statistics.txt")


def generate_config(filedir):
    if (os.path.isfile("config.json") and input("Reset config.json completely? [y/n]") != "y"):
        with open("config.json", "r") as f:
            config = json.load(f)
    else:
        print("No Config File found. Generating...")
        config = {}

    if (not "temp_directory" in config):
        config["temp_directory"] = "./tmp"

    if (not "file_directory" in config):
        config["file_directory"] = "./files"

    if (
        not "twitter" in config or
        not "consumer_key" in config["twitter"] or
        not "consumer_secret" in config["twitter"] or
        not "access_token" in config["twitter"] or
        not "access_token_secret" in config["twitter"]
    ):
        config["twitter"] = {
            "consumer_key": "",
            "consumer_secret": "",
            "access_token": "",
            "access_token_secret": ""
        }

    if (not "datasets" in config or input("Reset Dataset Config? [y/n]") == "y"):
        config["datasets"] = {}

    sg = statistics_generator.Statistics_generator(filedir)
    ds_data, _ = sg.generate()

    for ds in ds_data:
        translation_table = {}
        for label in ds_data[ds]["labels"]:
            translation_table[label] = [label]
        if not ds in config["datasets"]:
            config["datasets"][ds] = {
                "translation": translation_table, "download": True}
        else:
            if not "download" in config["datasets"][ds]:
                config["datasets"][ds]["download"] = True

            if "translation" in config["datasets"][ds]["translation"]:
                for i in config["datasets"][ds]["translation"]:
                    translation_table[i] = config["datasets"][ds]["translation"][i]
            config["datasets"][ds]["translation"] = translation_table

    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)


def clear_all(config):
    _clear_directory(config["file_directory"])
    _clear_directory(config["temp_directory"])


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
