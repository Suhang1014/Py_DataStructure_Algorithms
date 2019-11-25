# _*_ coding:utf-8 _*_
import sys


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    res = fib(n)
    print(res)


