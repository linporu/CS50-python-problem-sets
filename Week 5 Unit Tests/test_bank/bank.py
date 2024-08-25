def main():
    prompt = input("Greeting: ")
    output = value(prompt)
    print(f"${output}")


def value(greeting):
    edit_greeting = greeting.lower().strip()

    if edit_greeting.startswith("hello"):
        return 0

    elif edit_greeting.startswith("h"):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
