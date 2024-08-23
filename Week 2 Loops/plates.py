def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    char_list = list(str)

    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(char_list) < 2 or len(char_list) > 6:
        return False

    # All vanity plates must start with at least two letters.
    if not (char_list[0].isalpha() and char_list[1].isalpha()):
        return False

    # Iterate str
    for c in range(1, len(char_list)):

        # Numbers cannot be used in the middle of a plate; they must come at the end.
        if char_list[c - 1].isdigit() and not char_list[c].isdigit():
            return False

        if char_list[c - 1].isalpha() and char_list[c] == '0':
            return False

        # No periods, spaces, or punctuation marks are allowed.
        if not (char_list[c].isdigit() or char_list[c].isalpha()):
            return False

    return True


if __name__ == "__main__":
    main()
