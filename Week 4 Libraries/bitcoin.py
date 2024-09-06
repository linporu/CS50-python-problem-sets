import json
import requests
import sys

URL = ""

def main():
    n = parse_arguments()
    data = get_data()
    price = extract_price(data)
    amount = price * n
    print(f"${amount:,.4f}")


def parse_arguments():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    elif len(sys.argv) > 2:
        sys.exit("More than one command-line argument")

    try:
        return float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_data():
    # Get data from API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        return response.json()

    except requests.RequestException as e:
        sys.exit(e)


def extract_price(data):
    # You should use json.loads to parse a JSON string, but since data is already a dictionary, you don't need to use json.dump or json.loads at all. Instead, you can directly access the value and convert it to a float.
    try:
        return float(data["bpi"]["USD"]["rate"].replace(",", ""))
    except ValueError:
        sys.exit("Price is not float")


if __name__ == "__main__":
    main()
