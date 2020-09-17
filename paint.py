import math
from PIL import Image

im = Image.open("kacper.jpg")

pixels = im.load()
pixels_modified = {}
pixels_asci = {}

width, height = im.size

def define_brightness(pixel):
    return (pixel[0] + pixel[1] + pixel[2])/3

for column in range(width):
    for row in range(height):
        pixels_modified[column, row] = (define_brightness(pixels[column, row]))

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for column in range(width):
    for row in range(height):
        pixels_asci[column, row] = 3*chars[math.floor(
            (pixels_modified[column, row] / 255) * (len(chars)-1))]

for row in range(height):
    for column in range(width):
        print(pixels_asci[column, row], end="")
    print()