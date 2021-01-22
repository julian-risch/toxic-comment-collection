import datasets

for idx, dataset in enumerate(datasets.get_datasets()):
    dataset.fetch_files("./files/" + str(idx))