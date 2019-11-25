# _*_ coding:utf-8 _*_
import sys


def is_factor(a, b):
    if a % b == 0:
        return True
    return False


def shadow(t, ls):
    for a in ls:
        if is_factor(t, a):
            return False
    return True


def possible(ls):
    if 1 in ls:
        return False
    return True


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    vals = []
    res = []
    for i in range(n):
        # 读取每一行
        a = int(sys.stdin.readline().strip())
        vals.append(a)
    t = 0
    if possible(vals):
        while len(res) < 2:
            t += 1
            if shadow(t, vals):
                res.append(str(t))
        print(' '.join(res))
    else:
        print("Impossible")






