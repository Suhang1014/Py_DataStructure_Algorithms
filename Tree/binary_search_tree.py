# _*_ coding:utf-8 _*_
"""
二叉查找树
对于二叉查找树的每个节点Node，它的左子树中所有的关键字都小于Node的关键字，而右子树中的所有关键字都大于Node的关键字。
"""


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
        self.pre_order = []
        self.mid_order = []
        self.post_order = []

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def add(self, data):
        """添加节点"""
        new_node = Node(data)
        if self.isEmpty():
            self.root = new_node
        else:
            self.insert(self.root, new_node)

    def insert(self, cur_node, new_node):
        """插入节点"""
        # 递归函数，如果节点小于父节点，且父节点没有左子节点，则作为父节点的左子节点
        if new_node.data <= cur_node.data:
            # 如果父节点有左子节点，将节点插入到左子树中
            if cur_node.lchild:
                self.insert(cur_node.lchild, new_node)
            else:
                cur_node.lchild = new_node
                new_node.parent = cur_node
        elif new_node.data >= cur_node.data:
            if cur_node.rchild:
                self.insert(cur_node.rchild, new_node)
            else:
                cur_node.rchild = new_node
                new_node.parent = cur_node

    def search(self, cur_node, data):
        """
        :param cur_node:需要查找最小节点子树的根节点
        :param data:
        :return:
        """
        if self.isEmpty():
            print("二叉查找树为空，无法进行搜索！")
            return False
        else:
            def find(node, data):
                if node == None:
                    print("二叉搜索树中没有节点的值为", data, "的节点")
                    return False
                if node.data == data:
                    return node
                if data < node.data:
                    return find(node.lchild, data)
                if data > node.data:
                    return find(node.rchild, data)
            res = find(cur_node, data)
            return res

    def findMin(self, cur_node):
        """查找最小节点"""
        if self.isEmpty():
            print("二叉搜索树为空，无法进行搜索！")
            return False
        else:
            def fmin(node):
                if node.lchild:
                    return fmin(node.lchild)
                else:
                    return node
            return fmin(cur_node)

    def findMax(self, cur_node):
        """查找最大节点"""
        if self.isEmpty():
            print("二叉搜索树为空，无法进行搜索！")
            return False
        else:
            def fmax(node):
                if node.rchild:
                    return fmax(node.rchild)
                else:
                    return node
            return fmax(cur_node)

    def delete(self, cur_node, data):
        """
            input:cur_node:需要删除节点的树的根节点
                  data:需要删除节点的元素值
                三种情况
                (1)如果该节点是叶节点，直接删除
                (2)如果该节点只有一个子节点，该节点的父节点直接与其子节点连接
                (3)如果该节点有两个子节点，将其右子树的最小数据替代此节点的数据，并删除有右子树的最小数据
        """
        node = self.search(cur_node, data)
        if not node:
            print("删除操作：二叉搜索树没有节点的值为：", data, "无法执行删除操作")
            return False
        else:
            # 如果该节点是叶节点
            if node.lchild == None and node.rchild == None:
                if node == self.root:
                    self.root = None
                    print("二叉搜索树为空！")
                elif node.parent.lchild == node:
                    node.parent.lchild == None
                elif node.parent.rchild == node:
                    node.parent.rchild == None
            # 如果该节点只有一个子节点，其父节点直接指向其子节点
            if node.lchild and node.rchild == None:
                if node == self.root:
                    self.root.data = node.lchild.data
                    self.root.lchild = node.lchild.lchild
                else:
                    node.parent.lchild = node.lchild
                    node.lchild.parent = node.parent
            if node.rchild and node.lchild == None:
                if node == self.root:
                    self.root.data = node.lchild.data
                    self.root.lchild = node.lchild.lchild
                else:
                    node.parent.rchild = node.rchild
                    node.rchild.parent = node.parent
            # 如果该节点有两个子节点，将其右子树的最小数据替代此节点的数据，并删除有右子树的最小数据
            if node.rchild and node.lchild:
                min_right = self.findMin(node.rchild)
                node.data = min_right.data
                self.delete(node.rchild, min_right.data)

    def pre_order_travel(self,root):
        if root:
            self.pre_order.append(root.data)
            self.pre_order_travel(root.lchild)
            self.pre_order_travel(root.rchild)
        return self.pre_order

    def mid_order_travel(self,root):
        if root:
            self.mid_order_travel(root.lchild)
            self.mid_order.append(root.data)
            self.mid_order_travel(root.rchild)
        return self.mid_order

    def post_order_travel(self,root):
        if root:
            self.post_order_travel(root.lchild)
            self.post_order_travel(root.rchild)
            self.post_order.append(root.data)
        return self.post_order


if __name__ == "__main__":
    tree = BinarySearchTree()
    for data in range(10):
        tree.add(data)

    print("前序遍历：")
    print(tree.pre_order_travel(tree.root))

    print("中序遍历：")
    print(tree.mid_order_travel(tree.root))

    print("后序遍历：")
    print(tree.post_order_travel(tree.root))





