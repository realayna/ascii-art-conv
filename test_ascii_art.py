from PIL import Image
from pytest import*
from main import *

def test_resize_image():
    image = Image.new('RGB', (100,50))

    resized_image = resize_image(image, 80)
    assert resized_image.size == (80, 40)

    resized_image = resize_image(image, 120)
    assert resized_image.size == (120, 60)

def test_grayify():

    image = Image.new('RGB', (100, 50))

  
    gray_image = grayify(image)
    assert gray_image.mode == 'L'


def test_pixel_to_ascii():
    
    test_image = Image.new('L', (2, 2), color=128)
    pixels = list(test_image.getdata())

    
    ascii_str = pixel_to_ascii(test_image)
    expected_ascii_str = '++++'
    assert ascii_str == expected_ascii_str