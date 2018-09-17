'''
树形结构
'''

class Node(object):
    '''节点类'''
    def __init__(self, elem, lChild = None, rChild = None):
        self.elem = elem
        self.lChild = lChild #左子树
        self.rChild = rChild #又子树

class Tree(object):
    '''二叉树'''
    def __init__(self, node = None):
        self.root = node

    def add(self, item):
        '''添加子树'''
        '''
            思路
            1、先找到要添加元素的节点
            2、
        '''
        node = Node(item)

        if self.root is None:
            self.root = node
            return

        li = [self.root]
        while li:
            cur_node = li.pop(0)

            if cur_node.lChild is not None:
                li.append(cur_node.lChild)
            else:
                cur_node.lChild = node
                return

            if cur_node.rChild is not None:
                li.append(cur_node.rChild)
            else:
                cur_node.rChild = node
                return

    def breadth_travel(self):
        '''广度优先遍历'''
        if self.root is None:
            return

        li = [self.root]

        while li:
            cur_node = li.pop(0)
            print(cur_node.elem, end=' ')

            if cur_node.lChild is not None:
                li.append(cur_node.lChild)

            if cur_node.rChild is not None:
                li.append(cur_node.rChild)
        print(' ')



    def preorder(self, node):
        '''先序遍历'''
        if node is None:
            return

        print(node.elem, end=' ')
        self.preorder(node.lChild)
        self.preorder(node.rChild)

    def inorder(self, node):
        '''中序优先遍历'''
        if node is None:
            return

        self.preorder(node.lChild)
        print(node.elem, end=' ')
        self.preorder(node.rChild)

    def postorder(self, node):
        '''后续优先遍历'''
        if node is None:
            return

        self.preorder(node.lChild)
        self.preorder(node.rChild)
        print(node.elem, end=' ')


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" - ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
    print(" ")
