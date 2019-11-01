# _*_ coding:utf-8 _*_
"""
shuangxiang
"""
class Node:
    def __init__(self, data, pre = None, next = None):
        self.data = data
        self.pre = pre
        self.next = next


class DoubleLinkedList:
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head is None

    def __len__(self):
        p = self.head
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count

    def travel(self):
        """遍历整个链表"""
        p = p.head
        while p is not None:
            print(p.data, end=']')
            p = p.next

    def add_node(self, data):
        """在头部添加节点"""
        # 在头部添加，把原来的头部节点断开
        # 新的节点的地址指向原来节点的第一个位置，然后新的节点的元素设为头部
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        new_node.next.pre = new_node

    def append_node(self, data):
        """在尾部添加节点"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = new_node
            new_node.pre = p

    def insert_node(self, ind, data):
        """指定位置插入节点"""
        # 如果输入ind小于0，在头部插入
        if ind < 0:
            self.add_node(data)
        elif ind >= len(self):
            self.append_node(data)
        else:
            new_node = Node(data)
            p = self.head
            pre_ind = 0
            # 找到前一个位置
            while pre_ind < ind:
                p = p.next
                pre_ind += 1
            # 循环结束后，p指向ind位置
            new_node.next = p
            new_node.pre = p.pre
            p.pre.next = new_node
            p.pre = new_node

    def delete_node(self, ind):
        """删除ind位置节点"""
        if self.is_empty():
            return "The List is Empty!"
        if ind < 0 or ind > len(self) - 1:
            return "IndexError"
        else:
            p = self.head
            pre_ind = 0
            while pre_ind < ind:
                p = p.next
                pre_ind += 1
            p.pre.next = p.next
            p.next = p.pre

    def exist_node(self, data):
        """查找给定值的节点是否存在"""
        p = self.head
        while p is not None:
            if p.data == data:
                return True
            else:
                p = p.next
        return False

    def __repr__(self) -> str:
        nums = []
        current = self.head
        while current:
            nums.append(current.data)
            current = current.next
        return "<->".join(str(num) for num in nums)

    # 重写__iter__方法，方便for关键字调用打印值
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def print_all(self):
        current = self.head
        if current:
            print(f"{current.data}", end="")
            current = current.next
        while current:
            print(f"<->{current.data}", end="")
            current = current.next
        print("\n", flush=True)


if __name__ == '__main__':
    dl = DoubleLinkedList()
    for i in range(10):
        dl.append_node(i)
    dl. print_all()
    print(dl.exist_node(8))
    dl.add_node(99)
    dl.insert_node(2,100)
    dl.print_all()
    dl.delete_node(2)
    dl.print_all()



