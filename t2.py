# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:20:05 2019

@author: Administrator
"""

from PIL import Image


def plus(string):
    # Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
    return string.zfill(8)


def get_key(strr):
    # 获取要隐藏的文件内容
    with open(strr, "rb") as f:
        s = f.read()
        string = ""
        for i in range(len(s)):
            # 逐个字节将要隐藏的文件内容转换为二进制，并拼接起来
            # 1.先用ord()函数将s的内容逐个转换为ascii码
            # 2.使用bin()函数将十进制的ascii码转换为二进制
            # 3.由于bin()函数转换二进制后，二进制字符串的前面会有"0b"来表示这个字符串是二进制形式，所以用replace()替换为空
            # 4.又由于ascii码转换二进制后是七位，而正常情况下每个字符由8位二进制组成，所以使用自定义函数plus将其填充为8位
            string = string + "" + plus(bin(s[i]).replace('0b', ''))
    return string


def mod(x, y):
    return x % y


def opreations(n, key, count):
    e = 8
    print(count, len(key))
    return n - mod(n, (2 ** e)) + (int(key[count]) * (2 ** e))


def tests(h, w):
    # w_end = int(str(w)[-1])
    # white = [0, 1, 3, 4, 6, 7, 9, 0]
   # return ((w % 5 == 0) | ((w + 1) % 5 == 0) | ((w + 2) % 5 == 0) | ((w + 3) % 5 == 0)) | ((h % 5 == 0) | ((h + 1) % 5 == 0) | ((h + 2) % 5 == 0) | ((h + 3) % 5 == 0))
   return False


def dtr(h, w):
    return 255


# str1为载体图片路径，str2为隐写文件，str3为加密图片保存的路径
def func(str1, str2, str3):
    im = Image.open(str1)
    # 获取图片的宽和高
    width, height = im.size[0], im.size[1]
    print("width:" + str(width))
    print("height:" + str(height))
    count = 0
    # 获取需要隐藏的信息
    key = get_key(str2) + get_key(str2) + get_key(str2) + get_key(str2) + get_key(str2) + get_key(str2) + get_key(
        str2) + get_key(str2) + get_key(str2) + get_key(str2) + get_key(str2) + get_key(str2) + get_key(str2) + get_key(
        str2) + get_key(str2)
    keylen = len(key)
    for h in range(height):
        for w in range(width):
            pixel = im.getpixel((w, h))
            a = pixel[0]
            b = pixel[1]
            c = pixel[2]
            if count == keylen:
                break
            # 下面的操作是将信息隐藏进去
            # 分别将每个像素点的RGB值余2，这样可以去掉最低位的值
            # 再从需要隐藏的信息中取出一位，转换为整型
            # 两值相加，就把信息隐藏起来了

            if tests(h, w):
                a = dtr(h, w)
            else:
                a = opreations(a, key, count)
                count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break

            if tests(h, w):
                b = dtr(h, w)
            else:
                b = opreations(b, key, count)
                count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break

            if tests(h, w):
                c = dtr(h, w)
            else:
                c = opreations(c, key, count)
                count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break

            if count % 3 == 0:
                im.putpixel((w, h), (a, b, c))

    im.save(str3)


def main():
    # 原图
    old = "first.png"
    # 处理后输出的图片路径
    new = "second.png"
    # 需要隐藏的信息
    enc = "flag.txt"
    func(old, enc, new)


if __name__ == '__main__':
    main()
