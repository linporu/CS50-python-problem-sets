def main():

    price = 50
    due = int(price)

    while True:

        # Termination
        if due <= 0:
            print(f"Change Owed: {-due}")
            break

        # Print amount due
        print(f"Amount Due: {due}")

        # Start to insert coin
        coin = int(input("Insert coin: "))

        # Check for coin validation
        if coin not in [1, 5, 10, 25, 50]:
            coin = 0

        # Count and print remaining due
        due = due - coin


if __name__ == "__main__":
    main()
