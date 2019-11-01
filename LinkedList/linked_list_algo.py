"""
    1. 单链表反转
    2. 检测是否有环
    3. 有序链表合并
"""

from LinkedList.linked_list import SingleLinkedList

class Node:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

# 单链表反转
def reverse(head:Node):
    reversed_head = None
    current = head
    while current:
        reversed_head, reversed_head.next, current = current, reversed_head, current.next
    return reversed_head

# 判断链表内是否有环，快慢指针会在环内某一点相遇
def has_cycle(head: Node):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 有序链表合并
def merge_sort_list(l1:Node, l2:Node):
    # if l1 and l2:
    p1, p2 = l1, l2
    fake_head = Node(None)
    current = fake_head
    while p1 and p2:
        if p1.data <= p2.data:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    current.next = p1 or p2
    return fake_head.next
       
    # return l1 or l2

def print_all(head:Node):
        current = head
        if current:
            print(f"{current.data}", end="")
            current = current.next
        while current:
            print(f"->{current.data}", end="")
            current = current.next
        print("\n", flush=True)


if __name__ == '__main__':
    l = SingleLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)
    print(l)
    reversed_head = reverse(l.head)
    print_all(reversed_head)

    l1 = SingleLinkedList()
    for i in range(0, 15, 2):
        l1.insert_value_to_head(i)
    print(l1)
    l2 = SingleLinkedList()
    for i in range(1, 16, 2):
        l2.insert_value_to_head(i)
    print(l2)
    p3 = merge_sort_list(l1.head, l2.head)
    print_all(p3)
    
