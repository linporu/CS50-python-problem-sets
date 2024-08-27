def main():

    # Initial total value
    total = 0

    # Prompt for input
    while True:
        try:
            item = input("Item: ")
            item = item.strip().title()

            # Lookup menue
            item_price = lookup_menu(item)
            total += item_price
            print(f"Total: ${total:.2f}")

        except KeyError:
            continue

        except EOFError:
            print("")
            break


def lookup_menu(item):

    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    return menu[item]


if __name__ == "__main__":
    main()
