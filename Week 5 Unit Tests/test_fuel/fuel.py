def main():

    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except(ValueError, ZeroDivisionError):
            continue

    gauge_value = gauge(percentage)
    print(gauge_value)


def convert(fraction):

    x, y = fraction.split("/")

    try:
        # Handle input format
        if fraction.count("/") != 1:
            raise ValueError

        # x, y must be integers
        x = int(x)
        y = int(y)

        # Division
        division = x / y

        # x must <= y
        if x > y:
            raise ValueError

    except ValueError:
        raise ValueError

    except ZeroDivisionError:
        raise ZeroDivisionError

    else:
        return round(division * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"

    elif 1 < percentage < 99:
        return f"{percentage}%"

    elif percentage <= 1:
        return "E"


if __name__ == "__main__":
    main()
