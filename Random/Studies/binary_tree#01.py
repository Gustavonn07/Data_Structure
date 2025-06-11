class Node:
    def __init__(self, value=None, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, node=None):
        self._root = node

    def insert(self, node, value):
        if self._root is None:
            self._root = Node(value)

        elif value < node.value:
            if node.left is None:
                node.left = Node(value, parent=node)
            else:
                self.insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value, parent=node)
            else:
                self.insert(node.right, value)
