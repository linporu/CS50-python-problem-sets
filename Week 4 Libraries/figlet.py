import sys
import random
from pyfiglet import Figlet


def main():
    if len(sys.argv) == 1:
        font = None
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    prompt = input("Input: ")
    output = render_text(prompt, font)
    print(f"Output: \n{output}")


def render_text(prompt, font=None):
    figlet = Figlet()
    if font:
        figlet.setFont(font=font)
    else:
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font=random_font)
    return figlet.renderText(prompt)


if __name__ == "__main__":
    main()

# 輸入變數看起來有兩種狀況，但其實就是 font = None or font = argv[1]，這樣用一個 render_text() 就可以解決，不需要分兩個狀況的函數
# 可以考慮把 psudocode 化成流程圖，理解 function I/O
