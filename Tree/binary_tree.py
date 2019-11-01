"""
实现一般二叉树
前序遍历，中序遍历，后序遍历
"""


class TreeNode:
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def __init__(self):
        self.root = None
        self.val_ls = []
        self.pre_order = []
        self.mid_order = []
        self.post_order = []

    def add(self, data):
        """添加节点"""
        node = TreeNode(data)
        if self.root == None: # 如果树是空的，则对根节点赋值
            self.root = node
            self.val_ls.append(self.root)
        else:
            p = self.val_ls[0] # 此节点的子树还没有齐全
            if p.lchild == None:
                p.lchild = node
                self.val_ls.append(p.lchild)
            else:
                p.rchild = node
                self.val_ls.append(p.rchild)
                self.val_ls.pop(0) # 如果该节点存在右子树，将此节点丢弃

    def pre_order_search(self,root):
        """利用递归实现树的先序遍历"""
        if root:
            self.pre_order.append(root.data)
            self.pre_order_search(root.lchild)
            self.pre_order_search(root.rchild)
        return self.pre_order

    def mid_order_search(self,root):
        """递归中序遍历"""
        if root:
            self.mid_order_search(root.lchild)
            self.mid_order.append(root.data)
            self.mid_order_search(root.rchild)
        return self.mid_order

    def post_order_search(self,root):
        """递归后序遍历"""
        if root:
            self.post_order_search(root.lchild)
            self.post_order_search(root.rchild)
            self.post_order.append(root.data)
        return self.post_order


if __name__ == "__main__":
    tree = BinaryTree()
    for data in range(10):
        tree.add(data)

    print("前序遍历：")
    print(tree.pre_order_search(tree.root))

    print("中序遍历：")
    print(tree.mid_order_search(tree.root))

    print("后序遍历：")
    print(tree.post_order_search(tree.root))
