def main():
    prompt = input("Greeting: ").lower().strip()
    if prompt.startswith("hello"):
        print("$0")
    elif prompt.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
