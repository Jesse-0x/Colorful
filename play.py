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
        a = count % 345
        b = count % 234
        c = count % 234
        count += 1
        if random.randint(0, 1):
            im.putpixel((x, y), (a, b, c))
        else:
            im.putpixel((y, x), (a, b, c))
im.save("play.png")
