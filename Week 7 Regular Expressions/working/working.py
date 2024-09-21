import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?P<start>(\d(:[0-5]\d)?|(1[0-1])(:[0-5]\d)?|12(:00)?) [AP]M) to (?P<end>(\d(:[0-5]\d)?|1[0-1](:[0-5]\d)?|12(:00)?) [AP]M)$"

    if matches := re.search(pattern, s):
        start_time, start_AMPM = matches.group("start").split()
        end_time, end_AMPM = matches.group("end").split()

        if ":" in start_time:

            if start_AMPM == "AM":
                if start_time.split(":")[0] != "12":
                    start_hr = int(start_time.split(":")[0])
                else:
                    start_hr = 0

            elif start_AMPM == "PM":
                if start_time.split(":")[0] != "12":
                    start_hr = int(start_time.split(":")[0]) + 12
                else:
                    start_hr = 12

            start_min = int(start_time.split(":")[1])

        else:

            if start_AMPM == "AM":
                if start_time != "12":
                    start_hr = int(start_time)
                else:
                    start_hr = 0
            elif start_AMPM == "PM":
                if start_time != "12":
                    start_hr = int(start_time) + 12
                else:
                    start_time = 0

            start_min = 0

        if ":" in end_time:
            if end_AMPM == "AM":
                if end_time.split(":")[0] != "12":
                    end_hr = int(end_time.split(":")[0])
                else:
                    end_hr = 0
            elif end_AMPM == "PM":
                if end_time.split(":")[0] != "12":
                    end_hr = int(end_time.split(":")[0]) + 12
                else:
                    end_hr = 12

            end_min = int(end_time.split(":")[1])

        else:
            if end_AMPM == "AM":
                if end_time != "12":
                    end_hr = int(end_time)
                else:
                    end_hr = 0
            elif end_AMPM == "PM":
                if end_time != "12":
                    end_hr = int(end_time) + 12
                else:
                    end_hr = 12

            end_min = 0

        return f"{start_hr:02}:{start_min:02} to {end_hr:02}:{end_min:02}"

    raise ValueError


if __name__ == "__main__":
    main()
