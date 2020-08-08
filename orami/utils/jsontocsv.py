import csv
import json

import argparse

parser = argparse.ArgumentParser(description='Conver JSON to CSV')
parser.add_argument('-i', '--input', help='getting file input')
parser.add_argument('-o', '--output', help='getting file output')

args = parser.parse_args()
input_file = args.input
output_file = args.output

def read_json(filename):
    return json.loads(open(filename).read())

def write_csv(data, filename):
    with open(filename, 'w+') as outf:
        writer = csv.DictWriter(outf, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    print('Input File:', input_file)
    write_csv(read_json(input_file), output_file)
    print('Output File', output_file)