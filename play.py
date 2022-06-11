import random

from PIL import Image

im = Image.open("play.png")
print(im.format, im.size, im.mode)
pix = im.load()

width = im.size[0]
height = im.size[1]

count = 0

for x in range(width):
    for y in range(height):
        pixel = im.getpixel((x, y))
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)
        im.putpixel((x, y), (a, b, c))
        
im.save("play.png")
