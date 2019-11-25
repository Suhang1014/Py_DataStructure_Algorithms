# _*_ coding:utf-8 _*_
class Node:
    def __init__(self, data, parent=None, lchild=None, rchild=None):
        self.data = data
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild


class BinarySearchTree:
    def __init__(self):
        """初始化根节点"""
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def add(self, data):
        """添加节点"""
        new_node = Node(data)
        if self.is_empty():
            self.root = new_node
        else:
            self.insert(self.root, new_node)

    def insert(self, cur_node, new_node):
        """插入节点"""
        # 递归函数，如果节点大于父节点，且父节点没有右子节点，则作为父节点的右子节点
        if new_node.data >= cur_node.data:
            # 如果父节点有右子节点，将节点插入到右子树中
            if cur_node.rchild:
                self.insert(cur_node.rchild, new_node)
            else:
                cur_node.rchild = new_node
                new_node.parent = cur_node
        elif new_node.data <= cur_node.data:
            if cur_node.lchild:
                self.insert(cur_node.lchild, new_node)
            else:
                cur_node.lchild = new_node
                new_node.parent = cur_node

    def kthSmallest(self, root, k):
        mid_order = []

        def mid_order_travel(root):
            if root:
                mid_order_travel(root.lchild)
                mid_order.append(root.data)
                if len(mid_order) == k:
                    return
                mid_order_travel(root.rchild)
            else:
                return None
        mid_order_travel(root)
        return mid_order[k-1]


if __name__ == "__main__":
    num_list = [5,3,6,2,4,'null','null',1]
    k = 3
    tree = BinarySearchTree()
    for i in num_list:
        if i != 'null':
            tree.add(i)
    res = tree.kthSmallest(tree.root, k)
    print(res)


