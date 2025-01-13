# image_to_bytearray by Frederik Andersen
# Released under the MIT License (MIT). See LICENSE.
# Script to convert all .png and .jpg files in a folder to bytearray.
# The .png/.jpg files should have the correct color adjustments for the screen before this script is run.

import os
from PIL import Image

def convert_image_to_byte_array(image_path):
    # Open the image file
    img = Image.open(image_path)
    img = img.convert('RGB')

    # Define the color map
    color_map = {
        (0, 0, 0): 0x00,       # Black
        (255, 255, 255): 0x01, # White
        (0, 255, 0): 0x02,     # Green
        (0, 0, 255): 0x03,     # Blue
        (255, 0, 0): 0x04,     # Red
        (255, 255, 0): 0x05,   # Yellow
        (255, 128, 0): 0x06    # Orange
    }

    # Convert the image to a byte array
    byte_array = bytearray()
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            # Use the color map to get the color value, default to white if not found
            color_value = color_map.get(pixel, 0x01)
            byte_array.append(color_value)

    return byte_array

# Get the current directory
current_directory = os.getcwd()

# Iterate over all files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        image_path = os.path.join(current_directory, filename)
        byte_array = convert_image_to_byte_array(image_path)
        
        # Save the byte array to a .bin file with the same name as the image file
        bin_filename = os.path.splitext(filename)[0] + '.bin'
        with open(bin_filename, 'wb') as f:
            f.write(byte_array)

print("Conversion completed for all .png and .jpg files in the directory.")