from datetime import date, datetime
import inflect
import sys


def main():
    birthday = input("Date of birth: ")

    try:
        minutes = calculate_minutes(birthday)
        print(convert(minutes), end="")

    except Exception as e:
        print(e)
        sys.exit("Invalid input")


def calculate_minutes(birthday_str):
    today = date.today()
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()
    delta = today - birthday
    minutes = round(delta.days * 24 * 60)
    return minutes


def convert(s):
    p = inflect.engine()
    return f"{p.number_to_words(s, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()
