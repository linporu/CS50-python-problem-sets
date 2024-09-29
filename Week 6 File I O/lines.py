import sys


def main():
    if argv_is_valid():
        lines = file_reader(sys.argv[1])
        counter = line_counter(lines)
        print(counter)


def argv_is_valid():
    # Only 1 argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # It's a pythone file
    if sys.argv[1].endswith(".py"):
        return True
    else:
        sys.exit("Not a Python file")


def file_reader(file_name):
    try:
        with open(file_name) as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        sys.exit("File does not exist")


# line_counter 為了效能，同時在一次迴圈中 strip() 與計算行數，這犧牲一些 testability
def line_counter(lines):
    counter = 0
    for line in lines:
        # 除去空白與 \n
        line = line.strip()
        if not line.startswith("# ") and line != "":
            counter += 1
    return counter


if __name__ == "__main__":
    main()
