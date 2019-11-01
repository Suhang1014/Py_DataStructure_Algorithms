# _*_ coding:utf-8 _*_
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        """入队，尾部"""
        self.queue.append(item)

    def top(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def dequeue(self):
        """出队，队头"""
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def __repr__(self):
        return " ".join(f"{num}" for num in self.queue)


if __name__ == "__main__":
    aq = ArrayQueue()
    print(aq.is_empty())
    aq.enqueue(2)
    aq.enqueue(5)
    aq.enqueue(4)
    aq.enqueue(7)
    print(aq)
    item = aq.dequeue()
    print(item)