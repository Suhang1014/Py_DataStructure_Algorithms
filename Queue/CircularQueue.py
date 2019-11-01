# _*_ coding:utf-8 _*_
"""循环队列"""
"""
将队列的首尾相连接。这样当rear移动到LENGTH时，会再从0开始循环;
队空：rear == head
队满：牺牲一个空间，front前面不存数据，front指向队头，rear指向尾元素下一个位置，有 maxsize-1 个元素，即(rear+1) % maxsize == front
队列长度计算：1) rear > front: length = rear - front
            2) rear < front: (0 + rear) + (maxsize - front)
            3) 合并：(rear - front + maxsize) % maxsize
"""


class CircularQueue:
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0

    def size(self):
        # 当前队列长度
        return (self.rear - self.front + self.maxsize) % self.maxsize

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.maxsize == self.front

    def enqueue(self, item):
        if self.is_full():
            print("The Queue is full!")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.maxsize

    def dequeue(self):
        if self.is_empty():
            print("The Queue is empty!")
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            return item

    def showQueue(self):
        for i in range(self.maxsize):
            print(self.queue[i], end=',')
        print('')


if __name__ == "__main__":
    # 建立大小为15的循环队列
    q = CircularQueue(15)
    # 0~9入队列
    for i in range(10):
        q.enqueue(i)
    q.showQueue()
    # 删除队头的5个元素：0~4
    for i in range(5):
        q.dequeue()
    q.showQueue()
    # 从队尾增加8个元素：0~7
    for i in range(8):
        q.enqueue(i)
    q.showQueue()