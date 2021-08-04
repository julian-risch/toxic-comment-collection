import os
import ast
import pandas as pd

from . import datasets


class Statistics_generator:

    def __init__(self, filedir):
        self.filedir = filedir

    def generate(self, output_file=None):
        ds_data = self._collect_data()
        overall_data = self._calculate_overall_data(ds_data)
        if output_file:
            self._generate_output(output_file, ds_data, overall_data)
        return (ds_data, overall_data)

    def _generate_output(self, output_file, dataset_data, overall_data):
        str = self._generate_headline("Overall Statistics")
        str += self._generate_table(overall_data)
        str += self._generate_headline("Dataset Statistics")
        for i in dataset_data:
            str += i + "\n"
            str += self._generate_table(dataset_data[i], 4)
            str += "\n"

        with open(output_file, "w") as f:
            f.write(str)

    def _generate_headline(self, text):
        str = "#" * (len(text) +4) + "\n"
        str += "# " + text + " #"
        str += "\n" + "#" * (len(text) +4) + "\n\n"
        return str

    def _generate_table(self, data, indentation = 0):
        left_width = 0
        string = ""
        for i in data:
            left_width = max(len(str(i)), left_width)
        for i in data:
            string += " " * indentation
            string += str(i) + ":" + " " * (left_width -len(i) + 2)
            if type(data[i]) == dict:
                string += "\n"
                string += self._generate_table(data[i], indentation +4)
            else:
                string += str(data[i]) + "\n"
        return string

    def _collect_data(self):
        files = {}
        for idx, dataset in enumerate(datasets.get_datasets()):
            for file in dataset.files:
                file_path = os.path.join(self.filedir, dataset.name, file["name"])
                if (not os.path.isfile(file_path)):
                    continue
                files[file["name"]] = self._generate_file_statistics(file_path)
        return files
                

    def _generate_file_statistics(self, file):
        df = pd.read_csv(file, sep="\t")
        statistics = {}
        statistics["rows"] = len(df)
        statistics["file size"] = os.path.getsize(file)
        statistics["labels"] = self._get_label_count(df, "labels")
        return statistics

    def _get_label_count(self, df, column):
        counts = {}
        raw_counts = dict(df[column].value_counts())
        for i in raw_counts:
            for j in ast.literal_eval(i):
                if j not in counts:
                    counts[j] = 0
                counts[j] += int(raw_counts[i])
        return counts

    def _calculate_overall_data(self, dataset_data):
        rows = 0
        file_size = 0
        labels = {}
        for i in dataset_data:
            rows += dataset_data[i]["rows"]
            file_size += dataset_data[i]["file size"]
            for label, count in dataset_data[i]["labels"].items():
                if not label in labels:
                    labels[label] = 0
                labels[label] += count
        return {
            "rows" : rows,
            "file size" : file_size,
            "labels" : labels,
        }