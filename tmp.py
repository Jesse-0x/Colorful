import random


def play():
    if random.randint(1, 10) == 7:
        print("Chara開賣")
    else:
        print("Chara不開賣")


if __name__ == '__main__':
    play()
