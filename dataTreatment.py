import csv
from traceback import print_tb
import numpy as np

data_csv = rb'./datos.csv'
data = []

with open(data_csv, encoding='utf-8-sig') as dataFile:

    reader = csv.DictReader(dataFile)

    for row in reader:
        data.append(row)

dataFile.close()


def sumValues(col_name, value_of_intereset, value_to_sum):
    totalValue = 0

    for data_row in data:
        if data_row[col_name] == value_of_intereset:
            totalValue += int(data_row[value_to_sum])
    return totalValue


def calculate_total_victims(col_name):
    total = {}
    for row in data:
        value = row[col_name]
        if (value not in total):
            total[value] = sumValues(col_name, value, 'TOTAL_VICTIMAS')
    return total


total_victims = {}
cols = data[0].keys()

for col in cols:
    key_name = f'total_victims_{col}'
    if (key_name not in total_victims):
        total_victims[key_name] = calculate_total_victims(col)


def calculate_two_related_values_victims(first, second):
    total = {}
    total_victims = {}
    municipio_victims = []
    for row in data:
        first_value = row.get(first)
        second_value = row.get(second)
        victims = row.get('TOTAL_VICTIMAS')
        key = f'{first_value} en {second_value}'

        if (key not in total):
            total[key] = int(victims)
        else:
            total[key] += int(victims)

    # for key in total:
    #     year = key.split()[1]
    #     municipio = ' '.join(key.split()[3:])
    #     if (year and municipio) in key:
    #         municipio_victims.append({municipio: total[key]})
    #         total_victims[year] = municipio_victims

    return total


def calculate_two_related_values_cases(first, second):
    total = {}
    for row in data:
        first_value = row.get(first)
        second_value = row.get(second)
        victims = 1
        key = f'{first_value} en {second_value}'

        if (key not in total):
            total[key] = victims
        else:
            total[key] += victims

    return total


def calculate_two_related_cualitative_values(first, second, value_filter):
    total = {}

    for row in data:
        first_value = row.get(first)
        second_value = row.get(second)
        key = first_value

        if second_value == value_filter:
            if (key not in total):
                total[key] = 1
            else:
                total[key] += 1

    return total


def count_cases(value_of_interest):
    total_cases = {}
    for row in data:
        value = row.get(value_of_interest)
        if (value not in total_cases):
            total_cases[value] = 1
        else:
            total_cases[value] += 1
    return total_cases
