from PIL import Image
im = Image.open("first.png")
print(im.format, im.size, im.mode)
pix = im.load()

width = im.size[0]
height = im.size[1]

with open('flag.txt', 'rb') as f:
    binary = f.read()

flag = []
for i in list(binary):
    flag.append(int(bin(i).replace('0b', '').zfill(8), 2))

count = 0

for x in range(width):
    for y in range(height):
        r, g, b, a = im.getpixel((x, y))
        print(r, g, b, a)
        r = flag[count]
        print(r, g, b, a)
        im.putpixel((x, y), (r, g, b))
        count+=1
        if count >= len(flag):
            exit(0)