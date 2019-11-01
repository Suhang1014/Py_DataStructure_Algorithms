# _*_ coding:utf-8 _*_
class ArrayStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.extend(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else "Stack is empty!"

    def top(self):
        """返回栈顶元素"""
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def __repr__(self):
        return ' '.join(f"{num}]" for num in self.stack[::-1])


if __name__ == '__main__':
    new_stack = ArrayStack()
    new_stack.push([1,2,3,4,5,6,7])
    print(new_stack)
    print(new_stack.size())
    print(new_stack.top())
    print(new_stack.pop())
    print(new_stack.size())
    print(new_stack.pop())