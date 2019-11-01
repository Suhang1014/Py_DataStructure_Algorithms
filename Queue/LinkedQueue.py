# _*_ coding:utf-8 _*_
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


"""
定义一个头结点，左边指向队列的开头，右边指向队列的末尾，
这样就可以保证我们插入一个元素和取出一个元素都是O(1)的操作
"""


class Head:
    def __init__(self):
        self.left = None
        self.right = None


class LinkedQueue:
    def __init__(self):
        self.head = Head()

    def is_empty(self):
        if self.head.left:
            return False
        else:
            return True

    def enqueue(self, data):
        new_node = Node(data)
        p = self.head
        if p.right:
            # 如果head结点的右边不为None
            # 说明队列中已经有元素了
            temp = p.right
            p.right = new_node
            temp.next = new_node
        else:
            # 队列为空
            p.right = new_node
            p.left = new_node

    def dequeue(self):
        p = self.head
        if p.left and (p.left == p.right):
            # 最后一个元素
            temp = p.left
            p.left = p.right = None
            return temp.data
        elif p.left and (p.left != p.right):
            temp = p.left
            p.left = temp.next
            return temp.data
        else:
            # 队列为空，抛出查询错误
            return LookupError("Queue is empty!")

    def top(self):
        if self.head.left:
            return self.head.left.data
        else:
            # 队列为空，抛出查询错误
            return LookupError("Queue is empty!")


if __name__ == '__main__':
    queue = LinkedQueue()
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.top())
