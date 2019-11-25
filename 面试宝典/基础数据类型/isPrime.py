# _*_ coding:utf-8 _*_
"""
如果一个数不是素数，那么它可以分解成一系列小于它的素数乘积；
"""

prime_array = [1, 2, 3]

def isPrime(k):
    if k < 3:
        return True
    for i in range(len(prime_array)):
        if k > prime_array[i] and k % prime_array[i] == 0:
            return False
        prime_array.append(k)
        return True


def getPrimesInRange(n):
    primes = []
    for i in range(n+1):
        primes.append(True)
    for i in range(2, n+1):
        # 从第二个素数2开始，删除一轮下来后，如果接下来的primes[i]是True，那么其对应的整数就是素数
        if primes[i] == True:
            p = i
            j = 2
            # 把当前素数的倍数全部删去
            while p * j <= n:
                primes[p*j] = False
                j += 1
    for i in range(len(primes)):
        if primes[i] == True:
            print("{0},".format(i), end='')
    n = 100


if __name__ == '__main__':
    n = 200
    getPrimesInRange(n)








