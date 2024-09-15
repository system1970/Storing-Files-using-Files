# src/image_utils.py
from PIL import Image
import os
from .file_utils import create_folder

def create_binary_image(binary_string, output_file):
    """
    Creates a binary image (1-pixel height) representing the binary string and saves it.
    """
    width = len(binary_string)
    img = Image.new('1', (width, 1))  # Binary image (1-bit pixels)
    pixels = img.load()
    
    for i in range(width):
        pixels[i, 0] = int(binary_string[i])
    
    img.save(output_file + ".png")
    print(f"Image saved as {output_file}.png")

def create_binary_image_folder(binary_string, output_folder):
    """
    Creates a folder of binary images, each image representing a single bit from the binary string.
    """
    def create_fill_image(fill_value, output_file, width=1, height=1):
        """
        Creates a binary image filled with either 0 (black) or 1 (white) and saves it.
        """
        if fill_value not in [0, 1]:
            raise ValueError("fill_value must be 0 (black) or 1 (white)")
        
        img = Image.new('1', (width, height), fill_value)
        img.save(output_file)

    create_folder(output_folder)
    
    for pos, bit in enumerate(binary_string):
        create_fill_image(int(bit), f"./{output_folder}/{pos}.png", width=1, height=1)

def is_zero(image_path):
    """
    Checks if the given image contains only black pixels (0).
    """
    with open(image_path, 'rb') as file:
        img = Image.open(file).convert('1')
    pixels = img.getdata()
    return all(p == 0 for p in pixels)
