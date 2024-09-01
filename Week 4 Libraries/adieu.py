import sys


def main():

    # 收集名字
    name_list = collect_names()

    # 組合字串
    try:
        output = format_farewell_message(name_list)
    except ValueError:
        sys.exit("Invalid input")

    print(output)


def collect_names():
    name_list = []

    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            print()
            break

    return name_list


def format_farewell_message(name_list):
    string = "Adieu, adieu, to "

    list_len = len(name_list)

    # 若無輸入人名，跳出
    if list_len == 0:
        raise ValueError("No input")

    # 若只有一個人名
    elif list_len == 1:
        string += name_list[0]
        return string

    # 若有兩個人名
    elif list_len == 2:
        string += name_list[0] + " and " + name_list[1]
        return string

    # 若有兩個以上人名
    elif list_len > 2:
        # 累加名單至倒數第二個名字
        for i in range(0, list_len - 1):
            string += (name_list[i] + ", ")
        # 加入最後一個名字
        string += "and " + name_list[list_len - 1]
        return string

    else:
        raise ValueError("Unexpected error")


if __name__ == "__main__":
    main()
