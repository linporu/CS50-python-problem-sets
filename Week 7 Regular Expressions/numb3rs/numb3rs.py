import re
import sys


def main():
    result = validate(input("IPv4 Address: ").strip())
    print(result)


def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
    return bool(re.match(pattern, ip))


if __name__ == "__main__":
    main()
