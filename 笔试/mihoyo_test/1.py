# _*_ coding:utf-8 _*_
import sys


def max_delta(ls):
    length = len(ls)
    max_delta = 0
    for i in range(1, length):
        delta = ls[i] - ls[i - 1]
        if delta > max_delta:
            max_delta = delta
    return max_delta


if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip()
    w, h = tuple(map(int, line1.split()))
    n = int(sys.stdin.readline().strip())
    H = [0, h]
    W = [0, w]
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip().split()
        if line[0] == 'H':
            H.append(int(line[1]))
        else:
            W.append(int(line[1]))
    H.sort()
    W.sort()
    max_h_delta = max_delta(H)
    max_w_delta = max_delta(W)
    max_area = max_h_delta * max_w_delta
    print(max_area)






