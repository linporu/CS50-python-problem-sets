import random


PROBLEM_NUMBER = 10


def main():

    n = get_level()
    problems = generate_problems(n)
    score = solve_problems(problems)
    print(f"Score: {score}")


def get_level():
    # 請使用者輸入 1~3 的整數
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
    return level


def generate_integer(n):
    # 產生 n 位數的隨機整數
    max = 10 ** n - 1

    if n == 1:
        min = 0
    else:
        min = 10 ** (n - 1)

    return random.randint(min, max)


def generate_problems(n):
    # Create 10 questions in a problem list of dicts
    problems = []

    for _ in range(PROBLEM_NUMBER):
        question = {}
        x = generate_integer(n)
        y = generate_integer(n)
        answer = x + y
        question["question"] = f"{x} + {y} = "
        question["answer"] = answer
        problems.append(question)

    return problems


def solve_problems(problems):

    # Initiate score
    score = 0

    # Ask questions
    for question in problems:

        # 3 opportunities for each question
        opportunity = 3

        while True:
            print(question["question"], end="")
            try:
                user_ans = int(input())
                # 正確時算分，錯誤時達題機會 -1
                if user_ans == question["answer"]:
                    score += 1
                    break
                else:
                    print("EEE")
                    opportunity -= 1
            except ValueError:
                pass

            # Show answer if 3 incorrects
            if opportunity == 0:
                print(f"{question["question"]}{question["answer"]}")
                break

    return score


if __name__ == "__main__":
    main()
