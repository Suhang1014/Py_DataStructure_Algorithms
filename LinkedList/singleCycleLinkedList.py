class Node(object):
    def __init__(self, value:int, next=None):
        self.data = value
        self.next = next


class singleCycleLinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        """链表是否为空"""
        return self.head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        count = 1
        # 定义指针p
        p = self.head
        while p.next is not self.head:
            count += 1
            p = p.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return 0
        p = self.head
        while p.next is not self.head:
            print(p.data, end=" ")
            p = p.next
        print(p.data)

    def add(self, value):
        """链表头部添加元素"""
        node = Node(value)
        # 如果链表为空
        if self.is_empty():
            self.head = node
            # 指回自身
            node.next = node
            return
        # 如果不为空，遍历找到尾节点
        p = self.head
        while p.next is not self.head:
            p = p. next
        node.next = self.head
        self.head = node
        p.next = self.head

    def append(self, value):
        """尾部添加新节点"""
        if self.is_empty():
            self.add(value)
            return
        # 如果不为空，遍历找到尾节点
        p = self.head
        while p.next is not self.head:
            p = p.next
        node = Node(value)
        p.next = node
        node.next = self.head

    def insert(self, pos, value):
        """指定位置添加节点"""
        if pos <= 0:
            self.add(value)
        elif pos >= self.length():
            self.append(value)
        else:
            index = 0
            p = self.head
            while index < (pos - 1):
                index += 1
                p = p.next
            # while结束时，p指向pos的前置节点
            node = Node(value)
            node.next = p.next
            p.next = node

    def remove(self, value):
        """删除节点"""
        if self.is_empty():
            return
        # 定义pre记录当前节点前置节点
        pre = None
        p = self.head
        while p.next is not self.head:
            if p.data == value:
                # 删除当前节点
                # 如果pre为空，删掉的是头结点，需要让尾节点指向新的头结点
                if pre is None:
                    current = self.head
                    while current.next is not self.head:
                        current = current.next
                    # while结束，current指向尾节点
                    self.head = p.next
                    # 让尾节点指向新的头
                    current.next = self.head
                else:
                    pre.next = p.next
                return
            # pre 一直记录p的前置节点
            pre = p
            p = p.next
        # while循环处理不了尾节点，单独处理尾节点
        if p.data == value:
            # 如果pre为空， 证明当前只有一个节点，而且要删除这个节点
            if pre is None:
                self.head = None
            else:
                # 让尾节点的前置节点指向头结点
                pre.next = self.head

    def search(self, value):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        # 遍历查找item
        p = self.head
        while p.next is not self.head:
            if p.data == value:
                return True
            p = p.next
        # 单独处理尾节点
        if p.data == value:
            return True
        return False


if __name__ == '__main__':
    sll = singleCycleLinkedList()
    print(sll.length())
    print(sll.is_empty())
    sll.add(3)
    print(sll.is_empty())
    sll.add(2)
    sll.add(1)
    sll.travel()   # 123
    print(sll.length())
    sll.append(4)
    sll.travel()
    sll.insert(2, 6)
    sll.travel()
    sll.insert(-10, 7)
    sll.travel()
    sll.insert(10, 5)
    sll.travel()
    sll.remove(3)
    sll.travel()
    sll.remove(7)
    sll.travel()
    sll.remove(5)
    sll.travel()
    print(sll.search(1))
    print(sll.search(6))
    print(sll.search(4))
    print(sll.search(5))