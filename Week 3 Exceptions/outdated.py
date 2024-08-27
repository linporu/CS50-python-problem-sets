MONTH_DICT = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}


def main():

    while True:
        try:
            date = input("Date: ")
            year, month, day = get_date(date)

            if is_valid_date(year, month, day):
                print(f"{year}-{month:02}-{day:02}")
                return
            else:
                continue

        except ValueError:
            continue


def get_date(date):

    # Initial date
    year_num, month_num, day_num = 0, 0, 0

    # Check pattern MM/DD/YYYY
    if "/" in date:
        month, day, year = date.split("/")

        # Convert strings to integers
        month_num, day_num, year_num = int(month), int(day), int(year)

    # Check pattern Month DD, YYYY
    if "," in date:
        parts = date.split()

        # Get month_num
        month = parts[0]

        if month in MONTH_DICT:
            month_num = MONTH_DICT[month]

        # Get year_num
        year = parts[2]
        year_num = int(year)

        # Get day_num
        day = parts[1].replace(",", "")
        day_num = int(day)

    return year_num, month_num, day_num


def is_valid_date(year, month, day):
    return year > 0 and 1 <= month <= 12 and 1 <= day <= 31


if __name__ == "__main__":
    main()
