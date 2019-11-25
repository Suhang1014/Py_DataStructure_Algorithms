# _*_ coding:utf-8 _*_
import sys


def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if str2[i-1] == str1[j-1]:
                res[i][j] = res[i-1][j-1] + 1
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
    step = (len1 - res[-1][-1]) + (len2 - res[-1][-1])
    return step


if __name__ == "__main__":
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    str1, str2 = str1.lower(), str2.lower()
    print(lcs(str1, str2))




