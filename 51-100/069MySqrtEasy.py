# coding=utf-8


def mySqrt(x):
    i = 1
    while i * i <= x:
        i += 1
    return i - 1


if __name__ == '__main__':
    print(mySqrt(4))