import datasets
import os
import shutil
import sys
import getopt
import logging
import statisitics_generator
import json, csv
import datasets.helpers
import pandas as pd

TEMPDIR = "./tmp"
FILEDIR = "./files"

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

config = {}

def main(args):
    try:
        arguments = dict(getopt.getopt(args, "-r -? -o -s -g -d -c -t: -f:", ['reset', 'help', 'original', 'statistics', 'tempdir', 'filedir', 'genconfig', 'skipDownload', 'skipCombine'])[0])
    except:
        logging.error("Invalid argument!")
        print_help()
        return -1

    if ("--tempdir" in arguments or "-t" in arguments):
        tempdir = _parse_argument(arguments, "--tempdir", "-t")
    else: 
        tempdir = TEMPDIR

    if ("--filedir" in arguments or "-f" in arguments):
        tempdir = _parse_argument(arguments, "--filedir", "-f")
    else: 
        filedir = FILEDIR

    if ("--statistics" in arguments or "-s" in arguments):
        generate_statistics(filedir)
        exit()

    if ("--genconfig" in arguments):
        generate_config(filedir)
        exit()

    if ("--help" in arguments or "-?" in arguments):
        print_help()
        exit()
    
    if ("--reset" in arguments or "-r" in arguments):
        clear_all()
        exit()
    
    if not ("--skipDownload" in arguments or "-d" in arguments):
        unify = not ("--original" in arguments or "-o" in arguments)
        fetch_datasets(filedir, tempdir, unify_format=unify)

    if not ("--skipCombine" in arguments or "-c" in arguments):
        combine_datasets(filedir)

def print_help():
    print("""Usage: python3 main.py [-r][-?]
    
-r  --reset         Reset all existing files, deletes everything in folder 'tmp' and 'files'

-?  --help          Show this help

-t  --tempdir XXX   Set the temp directory to XXX (standard: ./tmp)

-f  --filedir XXX   Set the file directory to XXX (standard: ./files)

-o  --original      Download the datasets but don't process them

-s  --statistcs     Generates statistics about the downloaded datasets. Make sure to run
                    the script without the -s parameter before to download the datasets.
                    Does not work with unprocessed data (-o)""")


def combine_datasets(filedir, output_file_name="combined.tsv"):
    output_file = os.path.join(filedir, output_file_name)
    combined_df = pd.DataFrame()
    for dataset in datasets.get_datasets():
        for ds_file in dataset.files:
            df = pd.read_csv(os.path.join(filedir, dataset.name, ds_file["name"]), sep="\t")
            df.insert(loc=0, column="file_name", value=[ds_file["name"]] * df.count().max())
            df.insert(loc=0, column="file_language", value=[ds_file["language"]] * df.count().max())
            df.insert(loc=0, column="file_platform", value=[ds_file["platform"]] * df.count().max())
            df.drop(columns=["id"], inplace=True)
            combined_df = combined_df.append(df)
    combined_df.to_csv(output_file, index_label="id", quoting=csv.QUOTE_NONNUMERIC, sep="\t")

def fetch_datasets(filedir, tempdir, unify_format=True, translate_labels=True):
    clear_all()
    logging.info("Download Data and perform initial processing")
    max_suffix_length = 0
    for idx, dataset in enumerate(datasets.get_datasets()):
        max_suffix_length = _print_progress_bar(idx *2, len(datasets.get_datasets()) *2, "Download " + dataset.name, max_suffix_length)
        _clear_directory(tempdir)
        file = dataset.download(tempdir)
        max_suffix_length = _print_progress_bar(idx *2 +1, len(datasets.get_datasets()) *2, "Process " + dataset.name, max_suffix_length)
        dataset.valid_hash(file)
        dataset.process(file, os.path.join(filedir, dataset.name), tempdir)
        if unify_format:
            dataset.unify(os.path.join(filedir, dataset.name), translate_labels)
    _print_progress_bar(len(datasets.get_datasets()), len(datasets.get_datasets()), "Done", max_suffix_length)
    logging.info("Done fetching Datasets")

def generate_statistics(filedir):
    sg = statisitics_generator.Statisitics_generator(filedir)
    sg.generate("statistics.txt")

def generate_config(filedir):
    reset_twitter_api_keys = False
    reset_download_option = False
    reset_translation_table = False
    if (os.path.isfile("config.json") and input("Reset config.json completely? [y/n]") != "y"):
        with open("config.json", "r") as f:
            config = json.load(f)
    else:
        logging.info("No Config File found. Generating...")
        config = {}

    reset_twitter_api_keys = (
        not "twitter" in config or
        not "consumer_key" in config["twitter"] or
        not "consumer_secret" in config["twitter"] or
        not "access_token" in config["twitter"] or
        not "access_token_secret" in config["twitter"] or
        input("Reset API keys? [y/n] ") == "y"
    )
    if reset_twitter_api_keys:
        config["twitter"] = {
            "consumer_key": "xxxx",
            "consumer_secret": "xxxx",
            "access_token": "xxxx",
            "access_token_secret": "xxxx"
        }

    sg = statisitics_generator.Statisitics_generator(filedir)
    ds_data,_ = sg.generate()
    config["datasets"] = {}
    for ds in ds_data:
        translation_table = {}
        download = True
        for label in ds_data[ds]["labels"]:
            translation_table[label] = [label]
        config["datasets"][ds] = {
            "translation": translation_table,
            "download" : download
        }
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

def clear_all():
    logging.info("Clearing all existing Data")
    _clear_directory(TEMPDIR)
    _clear_directory(FILEDIR)
    
def _clear_directory(directory):
    logging.debug("Clearing Directory: " + str(directory))
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)

def _parse_argument(args, long_arg_name, short_arg_name):
    if (long_arg_name in args):
        if args[long_arg_name]:
            return args[long_arg_name]
        else:
            logging.error("Invalid arguments!")
            exit()
    elif (short_arg_name in args):
        if args[short_arg_name]:
            return args[short_arg_name]
        else:
            logging.error("Invalid arguments!")
            exit()
    else:
        raise ValueError("Neither long_arg_name nor short_arg_name are present in args!")

def _print_progress_bar(iteration, total, suffix='', max_suffix_length=0):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filledLength = int(50 * iteration // total)
    bar = '█' * filledLength + '-' * (50 - filledLength)
    suffix_string = suffix + (' ' * (max_suffix_length - len(suffix)))
    print(f'\rProgress: [{bar}] {percent}% {suffix_string}', end = '\r')
    if iteration == total: 
        print()
    return len(suffix_string)

if __name__ == '__main__':
    main(sys.argv[1:])
