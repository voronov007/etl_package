import csv


def load(file_path) -> csv.DictReader:
    # read txt file as dict like file
    data_file = csv.DictReader(open(file_path, 'r'), delimiter=";")
    return data_file
