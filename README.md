


## ASCII Art Generator

This Python script converts an image into ASCII art. It resizes the input image, converts it to grayscale, and then maps the pixel values to ASCII characters to create an ASCII representation of the image.

## Prerequisites

- Python 3.x
- Pillow (PIL) library (`pip install Pillow`)

## Usage

1. Clone this repository or download the `main.py` and `functions.py` files.

2. Place the image you want to convert into ASCII art in the same directory as `main.py`. Make sure to specify the image file path in the `main.py` script.

3. Run the script by executing `main.py`:

   ```bash
   python main.py
   ``` 
   
4.  The script will prompt you to enter the name of the output text file (include the ".txt" extension). This is where the ASCII art will be saved.
    
5.  Once the script finishes processing, you will find the ASCII art in the specified text file.
    

## Customization

You can customize the appearance of the generated ASCII art by modifying the `ASCII_CHARS` variable in the `functions.py` script. You can replace the characters in `ASCII_CHARS` with your preferred characters to achieve different visual effects.

python

`ASCII_CHARS = "@%#*-+=:. "` 

Additionally, you can change the width of the generated ASCII art by modifying the `new_width` parameter in the `main` function in `main.py`. A smaller `new_width` value will result in a more detailed but larger ASCII art image.
