# _*_ coding:utf-8 _*_
"""
题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。
"""

"""
方法一：哈希
"""
class Solution1:
    def duplicate(self, numbers):
        duplication = []
        if not numbers:
            return False
        temp = []
        for i in numbers:
            if i in temp:
                duplication.append(i)
            else:
                temp.append(i)
        return set(duplication)


if __name__ == "__main__":
    numbers = [2,3,1,0,2,5,3,3,3]
    s1 = Solution1()
    res = s1.duplicate(numbers)
    print(res)