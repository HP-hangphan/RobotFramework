import csv


def read_csv_file(file_path):
    with open(file_path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        customers = [row for row in reader]
        return customers
