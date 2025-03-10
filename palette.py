import logging

from PIL import Image
from time import perf_counter
from datetime import datetime

# Генерируем имя файла с текущей датой и временем
log_filename = datetime.now().strftime("logs_%Y-%m-%d_%H-%M-%S.txt")

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_filename),  # Запись в файл
        logging.StreamHandler()             # Дублирование в консоль
    ]
)

logging.info("Program has been started")

timer = perf_counter() # Start timer

width, height = 256, 255

# Create a new image with the specified mode
img = Image.new("RGB", (width, height))
pixels = img.load()

# @jit(nopython=True, fastmath=True)
def create_palette(mode, logg = False):

    if mode == "no_red":

        r, g, b, iterable = 0, 0, 0, 0

        for x in range(width):

            if b < 256:
                
                for y in range(height):
                    
                    pixels[x, y] = (r, g, b)

                    if logg:
                        iterable += 1
                        logging.info(f"Pixel at ({x}, {y}) is ({r}, {g}, {b}), {iterable}")

                    if g < 255:
                        g+= 1

                g = 1
                b += 1

    elif mode == "no_green":

        r, g, b, iterable = 0, 0, 0, 0

        for x in range(width):

            if b < 256:
                
                for y in range(height):

                    pixels[x, y] = (r, g, b)
                    
                    if logg:
                        iterable += 1
                        logging.info(f"Pixel at ({x}, {y}) is ({r}, {g}, {b}), {iterable}")

                    if r < 255:
                        r+= 1

                r = 1
                b += 1

    img.save(f"palette_{mode}.png")

# Create the palettes
create_palette("no_red")
create_palette("no_green")

print("This program took ", perf_counter() - timer, " seconds to run.") # Print the time it took to run the program

logging.info("Program finished.") # Log a message to the log file