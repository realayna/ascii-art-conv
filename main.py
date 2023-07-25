from PIL import Image, ImageDraw, ImageFont
import numpy as np
from functions import*


def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print("Error:", e)
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixel_to_ascii(image)

    width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join(ascii_str[i:i+width] for i in range(0, ascii_str_len, width))
    print(ascii_img)


    output_txt = input("Give the name to file (include txt extension): ")
    with open(output_txt, "w") as f:
        f.write(ascii_img)


if __name__ == "__main__":
    image_path = "stewie.png"  
    main(image_path)