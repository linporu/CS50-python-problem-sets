def main():

    # Create a grocery list in dict
    grocery_list = {}

    # Prompt for item
    while True:
        try:
            item = input()
            item = item.strip().upper()

            # Add item to list
            grocery_list = add_item(item, grocery_list)

        except EOFError:

            # Print sorted grocery list
            for item in sorted(grocery_list):
                print(f"{grocery_list[item]} {item}")

            break

    return 0


def add_item(item, grocery_list):

    if item in grocery_list:
        grocery_list[item] += 1
        return grocery_list

    else:
        grocery_list[item] = 1
        return grocery_list


if __name__ == "__main__":
    main()
