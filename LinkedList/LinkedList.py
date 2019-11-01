# _*_ coding:utf-8 _*_
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        """初始化"""
        self.head = None

    def __len__(self):
        """获取长度"""
        p = self.head
        length = 0
        while p:
            length += 1
            p = p.next
        return length

    def append_node(self, data):
        """追加节点"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node

    def get_node(self, ind):
        """根据位置获取节点的值，类似list索引"""
        ind = ind if ind >= 0 else len(self) + ind
        if ind >= len(self) or ind < 0:
            return None
        else:
            p = self.head
            while ind:
                p = p.next
                ind -= 1
            return p

    def set_node_value(self, ind, data):
        node = self.get_node(ind)
        if node:
            node.data = data

    def insert_node(self, ind, data):
        """找到ind前一个节点，在其后插入新节点"""
        new_node = Node(data)
        # p = self.head
        # 单独处理头部
        if ind == 0:
            new_node.next = self.head
            self.head = new_node
        # 获得ind前一节点位置
        else:
            pre_ind = ind - 1 if ind > 0 else len(self) + ind - 1
            pre_node = self.get_node(pre_ind)
            if pre_node:
                new_node.next = pre_node.next
                pre_node.next = new_node
            else:
                return False
    #
    # def delete_node(self, ind):
    #     node = self.get_node(ind)
    #     if node:

    def __repr__(self) -> str:
        nums = []
        current = self.head
        while current:
            nums.append(current.data)
            current = current.next
        return "->".join(str(num) for num in nums)

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
            print(f"->{current.data}", end="")
            current = current.next
        print("\n", flush=True)


if __name__ == '__main__':
    l = LinkedList()
    for i in range(10):
        l.append_node(i)
    l. print_all()
    n = l.get_node(-1)
    print(n.data)
    l.insert_node(2,100)
    l.print_all()







