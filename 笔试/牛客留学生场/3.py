# _*_ coding:utf-8 _*_
import sys
from fractions import Fraction


if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    n, m = tuple(map(int, line1.split()))
    group = []
    res = 0
    for i in range(2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        group.append(values)
    if n < m:
        res = '0/1'
    elif n > m:
        res = '1/0'
    else:
        res = Fraction(group[0][0], group[1][0])
    print(res)

