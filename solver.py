from PIL import Image

im = Image.open("second.png")

print(im.format, im.size, im.mode)
pix = im.load()

width = im.size[0]
height = im.size[1]

count = 0
h = 0
w = 0
for x in range(width):
    for y in range(height):
        if not (((x % 3 == 0) | ((y + 1) % 3 == 0)) | ((x % 3 == 0) | ((y + 1) % 3 == 0))):
            r, g, b, a = im.getpixel((x, y))
            print(r, g, b)
            im.putpixel((w, h), (r, g, b))
            w += 1
            if w == width:
                h += 1
                w = 0
im.save("out.png")