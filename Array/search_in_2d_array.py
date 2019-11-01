# _*_ coding:utf-8 _*_

"""
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

"""
方法一：迭代循环查找
时间复杂度：O(n^2)
"""
class Solution1:
    def search_in_2d_array(self, array, target):
        if not array:
            return
        row = len(array)
        col = len(array[0])
        for i in range(row):
            for j in range(col):
                if array[i][j] == target:
                    return True
        return False


"""
方法2：最优化的方式是从左下或者右上开始搜索
从右上开始搜索，如果数组中的数比该数要大，那么想左移动一位，
如果数组中的数比该数小，向下移动一位，
因为数组本身是从左到右依次增大，从上到下一次增大
"""
class Solution2:
    def search_in_2d_array(self, array, target):
        if not array:
            return
        row = len(array)
        col = len(array[0])
        # i，j标注当前位置，从右上角开始搜索
        i = 0
        j = col - 1
        while i < row and j >= 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False


if __name__ == '__main__':
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    array_blank = []
    target = 12
    target_2 = 20
    s1 = Solution1()
    s2 = Solution2()
    res_1 = [s1.search_in_2d_array(array_blank,target), s1.search_in_2d_array(array,target),
             s1.search_in_2d_array(array,target_2)]
    res_2 = [s2.search_in_2d_array(array_blank,target), s2.search_in_2d_array(array,target),
             s2.search_in_2d_array(array,target_2)]
    print(res_1, res_2)

