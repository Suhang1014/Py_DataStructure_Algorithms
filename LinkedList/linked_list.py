class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

class SingleLinkedList:
    '''单链表'''
    def __init__(self):
        self.head = None

    def find_by_value(self, value):
        p = self.head
        while p and p.data != value:
            p = p.next
        return p

    def find_by_index(self, index):
        p = self.head
        pos = 0
        while p and pos != index:
            p = p.next
            pos += 1
        return p

    def insert_node_to_head(self, new_node:Node):
        if new_node:
            new_node.next = self.head
            self.head = new_node

    def insert_value_to_head(self, value):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_after(self, node:Node, new_node:Node):
        if not node or not new_node:
            return
        new_node.next = node.next
        node.next = new_node

    def insert_value_before(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        if not self.head or not node or not new_node:
            return
        if self.head == node:
            self.insert_node_to_head(new_node)
            return
        current = self.head
        while current.next and current.next != node:
            current = current.next
        if not current.next:  # node is not even in the list
            return
        new_node.next = node
        current.next = new_node

    def delete_by_node(self, node: Node):
        if not self.head or not node:
            return
        if node.next:
            node.data = node.next.data
            node.next = node.next.next
            return
        # node is the last one or not in the list
        current = self.head
        while current and current.next != node:
            current = current.next
        if not current:  # node not in the list
            return
        current.next = node.next

    def delete_by_value(self, value: int):
        if not self.head or not value:
            return
        fake_head = Node(value + 1)
        fake_head.next = self.head
        prev, current = fake_head, self.head
        while current:
            if current.data != value:
                prev.next = current
                prev = prev.next
            current = current.next
        if prev.next:
            prev.next = None
        self.head = fake_head.next  # in case head.data == value

    def __repr__(self) -> str:
        nums = []
        current = self.head
        while current:
            nums.append(current.data)
            current = current.next
        return "->".join(str(num) for num in nums)

    # 重写__iter__方法，方便for关键字调用打印值
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


if __name__ == "__main__":
    l = SingleLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)
    node9 = l.find_by_value(9)
    l.insert_value_before(node9, 20)
    l.insert_value_before(node9, 16)
    l.insert_value_before(node9, 16)
    l.delete_by_value(16)
    node11 = l.find_by_index(3)
    l.delete_by_node(node11)
    l.delete_by_node(l.head)
    l.delete_by_value(13)
    print(l)
    for value in l:
        print(value)