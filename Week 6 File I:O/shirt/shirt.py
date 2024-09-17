from PIL import Image, ImageOps
import os
import sys


def main():
    if argv_is_valid():
        try:
            with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as shirt:
                img = ImageOps.fit(img, shirt.size)
                img.paste(shirt, (0, 0), shirt)
                img.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist")
    else:
        sys.exit()


def argv_is_valid():
    """Check if argv is valid"""
    # Only 2 argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # I/O are images
    if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")
    if not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")

    # I/O with the same formate
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")

    return True


if __name__ == "__main__":
    main()
