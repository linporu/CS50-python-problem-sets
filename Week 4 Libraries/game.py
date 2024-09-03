import random


def main():

    # Prompt for level "n"
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass

    # Get a random answer between 1 and n
    answer = random.randint(1, n)

    # Prompt user guess
    while True:
        try:
            guess = int(input("Guess: "))

            if guess < 0:
                continue

            if guess < answer:
                print("Too small!")

            elif guess == answer:
                print("Just right!")
                break

            elif guess > answer:
                print("Too large!")

        except ValueError:
            pass


if __name__ == "__main__":
    main()
