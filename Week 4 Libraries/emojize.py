import emoji
import re
import sys


def main():
    prompt = input("Input: ")

    # Find emoji_texts and return a list of text
    try:
        emoji_texts = re.findall(r':\w+:', prompt)
    except IndexError:
        sys.exit("Emoji does not exist.")

    # Find and replace emoji texts in the prompt
    for emoji_text in emoji_texts:
        emojized_text = emoji.emojize(emoji_text, language='alias')
        prompt = prompt.replace(emoji_text, emojized_text)

    # Print output
    print(f"Output: {prompt}")


if __name__ == "__main__":
    main()
