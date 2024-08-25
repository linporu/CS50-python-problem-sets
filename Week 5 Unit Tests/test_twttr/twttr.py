def main():
    str = input("Input: ")
    output = shorten(str)
    print(f"Output: {output}")


def shorten(word):
    str_new = ""
    for c in word:
        if not c.lower() in ["a", "e", "i", "o", "u"]:
            str_new += c
    return str_new


if __name__ == "__main__":
    main()
