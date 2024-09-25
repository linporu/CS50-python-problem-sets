import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    if matches := re.findall(pattern, s, re.IGNORECASE):
        return len(matches)
    else:
        return 0


if __name__ == "__main__":
    main()
