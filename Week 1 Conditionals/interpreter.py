def main():
    expression = input("Expression: ")
    num_1, operator, num_2 = expression.split(" ")

    match operator:
        case "+":
            answer = float(num_1) + float(num_2)
        case "-":
            answer = float(num_1) - float(num_2)
        case "*":
            answer = float(num_1) * float(num_2)
        case "/":
            if num_2 == 0:
                print("Error: 除數不應為零")
            else:
                answer = float(num_1) / float(num_2)

    print(answer)


if __name__ == "__main__":
    main()
