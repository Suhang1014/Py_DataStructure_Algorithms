# _*_ coding:utf-8 _*_
import sys
import math


def cal_Vsum(T, Vbp):
    if T <= 1:
        sum = 0
    elif 1 < T <= 5:
        sum = (T-1) * Vbp * 1.5
    elif 5 < T <= 10:
        sum = (T-5) * Vbp + (5-1) * Vbp * 1.5
    elif 10 < T <= 20:
        sum = (T-10) * Vbp * 0.5 + (10-5) * Vbp + (5-1) * Vbp * 1.5
    else:
        sum = (T-20) * Vbp * 0.2 + (20-10) * Vbp * 0.5 + (10-5) * Vbp + (5-1) * Vbp * 1.5
    return sum


def cal_Dsum(V, Dbp):
    if V <= 100:
        sum = V * Dbp
    elif 100 < V <= 125:
        sum = 100 * Dbp
    elif 100 < V <= 225:
        sum = (V-25) * Dbp
    elif 225 < V < 325:
        sum = 200 * Dbp
    elif 325 < V <= 625:
        sum = (V-125) * Dbp
    elif V > 625:
        base = 500 * Dbp
        extra = V - 625
        if math.floor(extra/100) % 2 != 0:
            sum = (math.floor(extra / 100) / 2 * 100 + extra % 100) * Dbp + base
        else:
            sum = math.floor(extra / 100) / 2 * 100 * Dbp + base
    return sum


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    num, t, vbp, v, dbp = tuple(map(int, line.split('|')))
    T, Vbp, V, Dbp = math.ceil(t/60), vbp/10, v/1024, dbp*10.24
    Vsum = cal_Vsum(T, Vbp)
    Dsum = cal_Dsum(V, Dbp)
    print(Vsum + Dsum)




