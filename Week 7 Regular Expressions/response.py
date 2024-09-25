import validators


def main():
    email_input = input("What's your email address? ")
    if validators.email(email_input):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
