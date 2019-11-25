# _*_ coding:utf-8 _*_
import sys


def str_matching(ori, tar):
    olen = len(ori)
    tlen = len(tar)
    count = 0
    for i in range(olen - tlen + 1):
        index = i
        for j in range(tlen):
            if ori[index] == tar[j]:
                index += 1
            else:
                break
            if index - i == tlen:
                count += 1
    return count


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    ori = line1.replace(" ", "")
    tar = sys.stdin.readline().strip()
    print(str_matching(ori, tar))


