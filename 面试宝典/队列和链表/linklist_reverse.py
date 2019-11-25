# _*_ coding:utf-8 _*_
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def append_node(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new_node

    def print_list(self, head):
        p = self.head
        while p is not None:
            print("{0}->".format(p.data), end="")
            p = p.next
        print("null")


def reverse(head):
    if head.next is None:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == '__main__':
    ls = LinkedList()
    for i in range(10):
        ls.append_node(i)
    ls.print_list(ls.head)
    rs = reverse(ls.head)
    while rs is not None:
        print("{0}->".format(rs.data),end="")
        rs = rs.next
    print("null")


