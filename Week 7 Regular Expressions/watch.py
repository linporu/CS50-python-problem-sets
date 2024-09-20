import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    pattern = r"^<iframe.*src=\"https?://(www\.)?youtube\.com/embed/(?P<src>[^\"]+)\".*\>\<\/iframe\>$"
    """
    ^<iframe                     # Start of iframe tag
    .*src="https?://             # src attribute with http or https
    (www\.)?youtube\.com/embed/  # YouTube domain
    (?P<src>[^"]+)               # Capture group for the video ID
    ".*>\<\/iframe>$             # End of src attribute and iframe tag
    """
    if matches := re.search(pattern, s):
        return "https://youtu.be/" + matches.group("src")
    return None


if __name__ == "__main__":
    main()
