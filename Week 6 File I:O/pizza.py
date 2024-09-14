import csv
from tabulate import tabulate
import sys


def main():
    if argv_is_valid():
        data = csvfile_reader(sys.argv[1])
        table = tabulate(data[1:], headers=data[0], tablefmt='grid')
        print(table)


def argv_is_valid():
    # Only 1 argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # It's a csv file
    if sys.argv[1].endswith(".csv"):
        return True
    else:
        sys.exit("Not a CSV file")

# Read file and return a list of data
def csvfile_reader(file_name):
    try:
        with open(file_name) as csvfile:
            reader = csv.reader(csvfile)

            data = [row for row in reader]
            return data
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
        main()
