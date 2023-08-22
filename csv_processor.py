import csv
import re


def summarize(files):
    boms = {}
    for name, file in files.items():
        content = read_csv(file)
        boms[name] = content

    return boms


def read_csv(csv_name):
    with open(csv_name) as csvfile:
        bom_reader = csv.DictReader(csvfile)
        return deduplicate(bom_reader)


def deduplicate(bom_reader):
    bom = {}
    for row in bom_reader:
        key = sanitize_part_name(row['Part name'])
        value = int(row['Quantity'])
        if key in bom:
            bom[key] += value
        else:
            bom[key] = value

    return bom


def sanitize_part_name(name):
    return re.sub(r"(\s?\(\d\)\s?)+?$", "", name).strip()

