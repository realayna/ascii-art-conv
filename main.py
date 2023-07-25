from PIL import Image
import numpy as np


ASCII_CHARS = "@%#*:/!?& "

def resize_image(img, n_width=100):
    width, height = img.size
    ratio=height/float(width)
    n_height = int(n_width*ratio)
    resized_image = img.resize((n_width, n_height))
    return resized_image

def grayify(img):
    return img.convert("L")

def pixel_to_ascii(img):
    pixels=img.getdata()
    ascii_str= ""
    for pixel_value in pixels:
        index = pixel_value * len(ASCII_CHARS) // 256
        ascii_str += ASCII_CHARS[index]
    return ascii_str


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

if __name__ == "__main__":
    image_path = "stewie.png"  
    main(image_path, 50)