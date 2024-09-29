import csv
import sys


def main():
    if argv_is_valid():
        students = csvfile_reader(sys.argv[1])
        students = split_name(students)
        csvfile_writer(sys.argv[2], students)
    else:
        sys.exit()


def argv_is_valid():
    """Check if argv is valid"""
    # Only 2 argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # I/O are csv files
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        return True
    else:
        sys.exit("Not CSV files")


def csvfile_reader(file_name):
    """Read file and return a list of dict"""
    try:
        with open(file_name, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            students = []
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
            return students
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")


def split_name(students):
    """Split names into first and last names, and return a new list of dict"""
    new_students = []
    for student in students:
        last_name, first_name = student["name"].split(", ")
        new_student = {"first": first_name, "last": last_name, "house": student["house"]}
        new_students.append(new_student)
    return new_students



def split_name_2(students):
    """
    Split names into first and last names, and return a new list of dict
    Renew list item by enumerate()
    """
    for index, student in enumerate(students):
        first_name, last_name = student["name"].split(", ")
        house = student["house"]
        students[index] = {"first": first_name, "last": last_name, "house": house}

    return students


def csvfile_writer(file_name, students):
    """
    Input a list of dict and output a csv file
    """
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first"] + ["last"] + ["house"])
        writer.writeheader()

        for row in students:
            writer.writerow(row)


if __name__ == "__main__":
    main()
