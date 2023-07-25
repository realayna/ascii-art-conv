from PIL import Image, ImageDraw, ImageFont
import numpy as np

ASCII_CHARS = "@%#*-+=:. "

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