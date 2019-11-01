"""
    基于链表实现的栈，链式栈
"""


class Node:
    def __init__(self, data: int, next=None):
        self.value = data
        self.next = next


class LinkedStack:
    def __init__(self):
        self.top: Node = None

    def is_empty(self):
        if self.top is None:
            return True
        return False

    def push(self, value: int):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
    
    def __repr__(self) -> str:
        current = self.top
        nums = []
        while current:
            nums.append(current.value)
            current = current.next
        return " ".join(f"{num}]" for num in nums)


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    print(stack.is_empty())
    for _ in range(3):
        stack.pop()
    print(stack)