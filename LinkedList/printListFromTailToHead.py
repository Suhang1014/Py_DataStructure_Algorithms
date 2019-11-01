# _*_ coding:utf-8 _*_
"""
输入一个链表，从尾到头打印
"""
from LinkedList.linked_list import SingleLinkedList

"""
方法：使用extend，在尾部插入，其实最关键在于[::-1],只不过输入数据多样化，有可能还是集合，所以转成列表
这个方法效率应该还可以，先存入vector，再反转vector
"""

class Solution1:
    def printListFromTailToHead(self, node):
        if not node:
            return []
        res = []
        while node.next is not None:
            res.extend([node.data])
            node = node.next
        # 单独处理尾节点
        res.extend([node.data])

        return res[::-1]