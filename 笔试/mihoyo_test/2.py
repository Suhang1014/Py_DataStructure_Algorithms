# _*_ coding:utf-8 _*_
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleCycleList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append_node(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def travel(self, n):
        score_ls = []
        if self.is_empty():
            return
        p = self.head
        while p.next != self.head:
            this_n = n
            cp = p
            score = 0
            while this_n > 0:
                score += cp.data
                cp = cp.next
                this_n -= 1
            score_ls.append(score)
            p = p.next
        final_score = 0
        while n > 0:
            final_score += p.data
            p = p.next
            n -= 1
        score_ls.append(final_score)
        return score_ls


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    vals = list(map(int, line.split()))
    linklist = SingleCycleList()
    for v in vals:
        linklist.append_node(v)
    max_score = 0
    for i in range(1, n + 1):
        score_ls = linklist.travel(i)
        this_max_score = max(score_ls)
        if this_max_score > max_score:
            max_score = this_max_score
    print(max_score)













