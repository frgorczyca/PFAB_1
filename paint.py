import math
from PIL import Image

im = Image.open("kacper.jpg")

pixels = im.load()
pixels_modified = {}
pixels_asci = {}

width, height = im.size

def define_brightness(pixel):
    return (pixel[0] + pixel[1] + pixel[2])/3

def define_brightness_minmax(pixel):
    return (min(pixel[0],pixel[1],pixel[2]) + max(pixel[0], pixel[1], pixel[0]))/2

def define_brightness_luminosity(pixel):
    return (0.21*pixel[0] + 0.71*pixel[1] + 0.07*pixel[2])

for column in range(width):
    for row in range(height):
        pixels_modified[column, row] = (define_brightness_luminosity(pixels[column, row]))

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for column in range(width):
    for row in range(height):
        pixels_asci[column, row] = 3*chars[math.floor(
            (pixels_modified[column, row] / 255) * (len(chars)-1))]

for row in range(height):
    for column in range(width):
        print(pixels_asci[column, row], end="")
    print()