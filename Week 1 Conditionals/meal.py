def main():
    str_time = input("What time is it? ")
    float_hour = convert(str_time)

    if 7.0 <= float_hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= float_hour <= 13.0:
        print("lunch time")
    elif 18.0 <= float_hour <= 19.0:
        print("dinner time")
    else:
        return


def convert(time):
    str_hour, str_minute = time.split(":")
    float_hour = float(str_hour) + (float(str_minute) / 60)
    return float_hour


if __name__ == "__main__":
    main()
