import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?P<start>(\d(:[0-5]\d)?|(1[0-1])(:[0-5]\d)?|12(:00)?) [AP]M) to (?P<end>(\d(:[0-5]\d)?|1[0-1](:[0-5]\d)?|12(:00)?) [AP]M)$"

    if matches := re.search(pattern, s):

        start_hr, start_min, start_AM_or_PM = parse_string(matches.group("start"))
        start_hr = convert_hr(start_hr, start_AM_or_PM)

        end_hr, end_min, end_AM_or_PM = parse_string(matches.group("end"))
        end_hr = convert_hr(end_hr, end_AM_or_PM)

        return f"{start_hr:02}:{start_min:02} to {end_hr:02}:{end_min:02}"

    raise ValueError


def parse_string(time_string):
    time, AM_or_PM = time_string.split()

    if ":" in time:
        hr, min = time.split(":")
        return hr, min, AM_or_PM

    else:
        hr = time
        min = 0
        return hr, min, AM_or_PM


def convert_hr(hr, AM_or_PM):
    if AM_or_PM == "AM":
        hr = int(hr) if hr != "12" else 0  # Handle 12:00 AM
        return hr

    else:
        hr = int(hr) + 12 if hr != "12" else 12  # Handle 12:00 PM
        return hr


if __name__ == "__main__":
    main()
