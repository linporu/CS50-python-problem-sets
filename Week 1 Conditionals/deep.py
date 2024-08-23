def main():
    answer = input("What is the Answer to the Freat Question of Life, the Universe, and Everything? ").lower().strip()
    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


if __name__ == "__main__":
    main()
