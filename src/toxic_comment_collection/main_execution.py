import importlib
import os
import shutil
from typing import List

import json
import csv
import pandas as pd

from . import datasets
from .datasets import helpers, dataset, get_dataset_by_name
from .statistics_generator import Statistics_generator


def generate_statistics(dataset_directory_path):
    generate_statistics_file(dataset_directory_path)


def get_all_datasets(*, config_path=None, reset=False, skip_combine=False, skip_download=False, api_config_path=None):
    config = __get_config(config_path)
    api_config = __get_api_config(api_config_path)

    if reset:
        clear_all(config)
        return

    if not skip_download:
        max_suffix_length = download_datasets(config)
        max_suffix_length = process_datasets(config, api_config, max_suffix_length)
    else:
        max_suffix_length = 0

    max_suffix_length = unify_datasets(config, max_suffix_length)

    if not skip_combine:
        combine_datasets(config)


def get_dataset(name, *, config_path=None, skip_download=False, api_config_path=None):
    config = __get_config(config_path)
    api_config = __get_api_config(api_config_path)
    dataset = get_dataset_by_name(name)

    if not dataset:
        raise RuntimeError(f"Dataset: {name} not found")
    if not skip_download:
        file = dataset.download(os.path.join(config["raw_directory"], dataset.name))
        dataset.valid_hash(file)
    __process_dataset(config, dataset, api_config)
    __unify_dataset(config, dataset)


def combine_datasets(config, output_file_name="combined.tsv"):
    filedir = config["file_directory"]
    output_file = os.path.join(filedir, output_file_name)
    combined_df = pd.DataFrame()
    for dataset in __filter_datasets_from_config(config):
        for ds_file in dataset.files:
            try:
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
            except:
                print("Could not add {0} to the combined dataset. Continuing with next file.".format(ds_file["name"]))
    combined_df.to_csv(output_file, index_label="id",
                       quoting=csv.QUOTE_NONNUMERIC, sep="\t")


def unify_datasets(config, max_suffix_length=0):
    _clear_directory(config["file_directory"])
    possible_datasets = __filter_datasets_from_config(config)
    for idx, dataset in enumerate(possible_datasets):
        max_suffix_length = _print_progress_bar(idx + len(possible_datasets) * 2, len(
            possible_datasets) * 3, "Unify " + dataset.name, max_suffix_length)

        __unify_dataset(config, dataset)


    _print_progress_bar(len(possible_datasets) * 3, len(possible_datasets) * 3, "Done", max_suffix_length)
    return max_suffix_length


def __unify_dataset(config, dataset):
    try:
        for ds_file in dataset.files:
            helpers.copy_file(os.path.join(config["raw_directory"], dataset.name + "_dir", ds_file["name"]),
                              os.path.join(config["file_directory"], dataset.name, ds_file["name"]))

        dataset.unify(config, dataset.name)
    except Exception:
        print("\nCould not unify {0}. Continuing with next dataset.".format(dataset.name))


def process_datasets(config, api_config, max_suffix_length=0):
    possible_datasets = __filter_datasets_from_config(config)
    for idx, dataset in enumerate(possible_datasets):
        max_suffix_length = _print_progress_bar(
            idx + len(possible_datasets), len(possible_datasets) * 3, "Process " + dataset.name, max_suffix_length)

        __process_dataset(config, dataset, api_config)

    return max_suffix_length


def __process_dataset(config, dataset, api_config):
    _clear_directory(config["temp_directory"])
    tmp_file_name = os.path.join(config["temp_directory"], dataset.name)
    helpers.copy_file(os.path.join(config["raw_directory"], dataset.name), tmp_file_name)
    try:
        dataset.process(tmp_file_name, os.path.join(config["raw_directory"], dataset.name + "_dir"), api_config)
    except Exception as e:
        print("\nError while processing {0}. Continuing with next one.".format(dataset.name))
        raise e


def download_datasets(config, max_suffix_length=0) -> int:
    _clear_directory(config["raw_directory"])
    possible_datasets = __filter_datasets_from_config(config)

    for idx, dataset in enumerate(possible_datasets):
        max_suffix_length = _print_progress_bar(
            idx, len(possible_datasets) * 3, "Download " + dataset.name, max_suffix_length)

        if dataset.name in config["data_sources"] and config["data_sources"].get(dataset.name)["download"]:
            file = dataset.download(os.path.join(config["raw_directory"], dataset.name))
            dataset.valid_hash(file)

    return max_suffix_length


def generate_statistics_file(filedir):
    sg = Statistics_generator(filedir)
    sg.generate("statistics.txt")


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


def __get_api_config(config_path):
    if config_path:
        return __get_config_from_path(config_path)
    return None


def __get_config(config_path):
    if config_path:
        config = __get_config_from_path(config_path)
    else:
        config = json.loads(importlib.resources.read_text(__package__, "config.json"))
    return config


def __get_config_from_path(config_path):
    try:
        with open(config_path, 'r') as config_file:
            return json.loads(config_file.read())
    except Exception:
        print(
            "Failure loading config.json. Run the following command to reset config.json:\n\n\tmain.py --genconfig")  # TODO: remove option to generate config?


def __filter_datasets_from_config(config):
    all_possible_datasets: List[dataset.Dataset] = datasets.get_datasets()
    return list(filter(lambda dataset: dataset.name in config["data_sources"], all_possible_datasets))
