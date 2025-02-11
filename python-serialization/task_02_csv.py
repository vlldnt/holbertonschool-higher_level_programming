#!/usr/bin/python3
'''Reading data CSV and converting in JSON suing serialize'''


import csv
import json


def convert_csv_to_json(csv_filename):
    '''Convert a CSV file in JSON file'''
    try:
        with open(csv_filename, "r") as csv_file:
            csv_file = csv.DictReader(csv_file)
            data = list(csv_file)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
