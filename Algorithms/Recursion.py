# _*_ coding:utf-8 _*_
"""递归"""
"""
- 递归需要满足三个条件：1. 一个问题的解可以分解为几个子问题的解；
                     2. 该子问题除了数据规模，求解思路完全一样；
                     3. 存在递归终止条件；
- 编写关键：写出'递推公式'，找到终止条件。
- 警惕堆栈溢出，最大深度较小时在代码中限制递归调用的最大深度。
- 警惕重复计算
- 时间空间复杂度太高
"""


def fibonacci(n):
    """斐波那契数列"""
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    """阶乘"""
    if n == 1:
        return 1
    return n * factorial(n - 1)


def permutation(arr, pos, end):
    """全排列：确定第1位，对剩余n-1位进行全排列，确定第2位，对n-2位进行全排列..."""
    if pos == end:
        print(arr)
    else:
        for index in range(pos, end):
            arr[index], arr[pos] = arr[pos], arr[index]
            permutation(arr, pos+1, end)
            # 恢复原样
            arr[index], arr[pos] = arr[pos], arr[index]


if __name__ == "__main__":
    # n = int(input().strip())
    # print(fibonacci(n))
    # print(factorial(n))
    arr = [1,2,3,4]
    permutation(arr, 0, len(arr))