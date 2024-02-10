import sys
import csv


data = list(map(lambda x: x.strip().split('\t'), sys.stdin))

with open('plantis.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['nomen, definitio, pluma, Russian nomen, familia, Russian nomen familia'])
    writer.writerows(data)
