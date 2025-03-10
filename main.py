import numpy as np
import logging

from PIL import Image

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
# Load the image
width, height = 512, 512

def create_palette(mode):

    # Create a new image with the specified mode
    img = Image.new("RGB", (width, height))
    pixels = img.load()

    # Fill the image with a gradient of colors
    for x in range(width):
        for y in range(height):
            
            # Calculate the color based on the mode
            val1 = x - 255
            val2 = y - 255

            if mode == "no_red":
                
                # Set green and blue to a value between 0 and 255
                r = 0
                g = max(0, min(255, val1 + 255))
                b = max(0, min(255, val2 + 255))

                
            
            elif mode == "no_green":
                
                # Set red and blue to a value between 0 and 255
                g = 0
                r = max(0, min(255, val1 + 255))
                b = max(0, min(255, val2 + 255))
                
                

            else:

                # Logging
                logging.info("undefined, please choose 'no_red' or 'no_green' in func options")

            pixels[x, y] = (r, g, b) # Set the RGB value of the pixel at (x,y)

    img.save(f"palette_{mode}.png") # Save image into progect directory

# Create the palettes
create_palette("no_red")
create_palette("no_green")