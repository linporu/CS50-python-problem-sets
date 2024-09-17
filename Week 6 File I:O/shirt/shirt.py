from PIL import Image
import os
import sys


def main():
    if argv_is_valid():
        try:
            with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as shirt:
                img, shirt = resize_img(img, shirt)
                img = crop_img(img)
                print("Image size after cropping:", img.size)
                print("Shirt size after resizing:", shirt.size)
                img.paste(shirt, (0, img.size[1] - shirt.size[1]), shirt)
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


def crop_img(image):
    """Crop image into 1200*1200px from center"""

    # Get the dimensions of the image
    width, height = image.size

    # Define the crop box (left, upper, right, lower)
    left = 0
    upper = (height - width) // 2
    right = width
    lower = width + (height - width) // 2

    # Crop the image
    cropped_image = image.crop((left, upper, right, lower))

    return cropped_image


def resize_img(img_1, img_2):
    """
    Resize img_2 to fit in img_1, while img_1 remain unchanged
    """

    # Calculate the new size of img_2 while maintaining the aspect ratio
    img_1_width, img_1_height = img_1.size
    img_2_width, img_2_height = img_2.size
    aspect_ratio = img_2_width / img_2_height

    if img_1_width / img_1_height > aspect_ratio:
        new_img_2_width = int(img_1_height * aspect_ratio)
        new_img_2_height = img_1_height
    else:
        new_img_2_width = img_1_width
        new_img_2_height = int(img_1_width / aspect_ratio)

    img_2 = img_2.resize((new_img_2_width, new_img_2_height))

    return img_1, img_2


if __name__ == "__main__":
    main()
