import sys
import math


def not_in(x):
    if 0 <= abs(x) <= 100000:
        return False
    return True

def reasonable(ls):
    x, y, a, b, v = ls[0], ls[1], ls[2], ls[3], ls[4]
    if v < 1 or v > 10 or not_in(x) or not_in(y) or not_in(a) or not_in(b):
        return False
    return True


def time(ls):
    x, y, a, b, v = ls[0], ls[1], ls[2], ls[3], ls[4]
    if v < 1 or v > 10 or not_in(x) or not_in(y) or not_in(a) or not_in(b):
        return False
    d = math.sqrt((x - a)**2 + (y - b)**2)
    t = round(d / v, 3)
    return t


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    if n < 1 or n > 100000:
        print('n 超过范围！')
    if 1 <= n <= 100000:
        res = []
        for i in range(n):
            line = sys.stdin.readline().strip()
            values = list(map(int, line.split()))
            if reasonable(values):
                t = time(values)
                res.append(t)
            else:
                break
        if len(res) != 0:
            print(max(res))


