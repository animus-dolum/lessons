import csv
from csv import reader, writer


with open('price.csv', 'r', encoding='utf-8') as f:
    reader = reader(f, delimiter=';', quotechar='"')
    data = list(reader)
