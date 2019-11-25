# _*_ coding:utf-8 _*_
import sys
from random import random


def sum_square(x, y):
    return x**2 + y**2


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    if n != 0:
        i = 0
        m = 0
        while i <= n:
            x = random()
            y = random()
            res = sum_square(x, y)
            if res <= 1:
                m += 1
            i += 1
        pi = 4 * m / n
    else:
        pi = 0
    print(pi)
