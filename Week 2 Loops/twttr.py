def main():

    str = input("Input: ")
    output = de_vowels(str)
    print(f"Output: {output}")


def de_vowels(str):

    str_new = ""
    for c in str:
        if not c.lower() in ["a", "e", "i", "o", "u"]:
            str_new += c
    return str_new


if __name__ == "__main__":
    main()
