import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"^um$|^um[^a-zA-Z]|[^a-zA-Z]um$|[^a-zA-Z]um[^a-zA-Z]"
    if matches := re.findall(pattern, s, re.IGNORECASE):
        return len(matches)
    else:
        return 0


if __name__ == "__main__":
    main()
