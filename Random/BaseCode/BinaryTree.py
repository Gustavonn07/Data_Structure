from abc import ABC, abstractmethod


class TreeADT(ABC):

    @abstractmethod
    def insert(self, value):
        """Insere <value> na Ã¡rvore"""
        pass

    @abstractmethod
    def empty(self):
        """Verifica se a Ã¡rvore estÃ¡ vazia"""
        pass

    @abstractmethod
    def root(self):
        """Retorna o nÃ³ raiz da Ã¡rvore"""
        pass


class BinaryNode:

    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def empty(self):
        return not self._data

    def data(self):
        return self._data

    def left_node(self):
        return self._left

    def right_node(self):
        return self._right

    def parent_node(self):
        return self._parent

    def set_parent(self, p):
        self._parent = p

    def set_left_node(self, l):
        self._left = l

    def set_right_node(self, r):
        self._right = r

    def set_data(self, d):
        self._data = d

    def has_left_child(self):
        result = False
        if self.left_node():
            result = True
        return result

    def has_right_child(self):
        result = False
        if self.right_node():
            result = True
        return result

    def __str__(self):
        return self._data.__str__()

    def __eq__(self, other):
        result = False
        if isinstance(other, BinaryNode):
            if self._data == other._data:
                result = True
        return result

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        result = False
        if isinstance(other, BinaryNode):
            if self._data <= other._data:
                result = True
        return result

    def __lt__(self, other):
        result = False
        if isinstance(other, BinaryNode):
            if self._data < other._data:
                result = True
        return result


class BinaryTree(TreeADT):

    def __init__(self, data=None, node: BinaryNode = None):
        if node:
            self._root = node
        else:
            self._root = BinaryNode(data)

    def empty(self):
        return not self._root.data()

    def root(self):
        return self._root

    def minimum(self, root):
        result = root
        while result.left_node():
            result = result.left_node()
        return result

    def min_rec(self, root):
        if not root.left_node():
            return root
        else:
            self.min_rec(root.left_node())

    def maximum(self, root):
        result = root
        while result.right_node():
            result = result.right_node()
        return result

    def max_rec(self, root):
        if not root.right_node():
            return root
        else:
            self.max_rec(root.right_node())

    def _insert_node(self, node):
        if self.empty():
            self._root = node
            return self._root
        else:
            return self.__insert_children(self._root, node)

    def insert(self, elem):
        node = BinaryNode(elem)
        if self.empty():
            self._root = node
            return self._root
        else:
            return self.__insert_children(self._root, node)

    def __insert_children(self, root: BinaryNode, node):
        if node <= root:
            if not root.has_left_child(): # nÃ£o existe nÃ³ a esquerda (caso base)
                root.set_left_node(node)
                root.left_node().set_parent(root)
                return root.left_node()
            else:
                return self.__insert_children(root.left_node(), node)  # sub-Ã¡rvore esquerda
        else:
            if not root.has_right_child():  # nÃ£o existe nÃ³ a direta (caso base)
                root.set_right_node(node)
                root.right_node().set_parent(root)
                return root.right_node()
            else:
                return self.__insert_children(root.right_node(), node)  # sub-Ã¡rvore direta

    def insert_iterative(self, elem):
        node = BinaryNode(elem)
        if self.empty():
            self._root = node
            return self._root

        current = self._root
        parent = None
        while current:
            parent = current
            if node <= current:
                current = current.left_node()
            else:
                current = current.right_node()

        node.set_parent(parent)
        if node <= parent:
            parent.set_left_node(node)
        else:
            parent.set_right_node(node)
        return node

    def search(self, value: int):
        node = BinaryNode(value)
        if not self.empty():
            return self.__search_children(self._root, node)
        else:
            return False, node

    def __search_children(self, root, node):
        if not root:
            return False, node
        if root == node:
            return True, root
        elif node < root:
            return self.__search_children(root.left_node(), node)
        else:
            return self.__search_children(root.right_node(), node)

    def search_iterative(self, value: int):
        node = BinaryNode(value)
        root = self._root
        while root and root != node:
            if node < root:
                root = root.left_node()
            else:
                root = root.right_node()

        if root:
            return True, root
        else:
            return False, node

    def successor(self, node):
        belongs, n = self.search_iterative(node.data())
        if belongs:
            if n.right_node():
                return self.minimum(n.right_node())
            else:
                return n
        else:
            return None

    def delete(self, value):
        belongs, z = self.search_iterative(value)
        if belongs:
            if not z.has_left_child() or not z.has_right_child():
                y = z
            else:
                y = self.successor(z)

            if y.left_node():
                x = y.left_node()
            else:
                x = y.right_node()

            if x:
                x.set_parent(y.parent_node())

            if not y.parent_node():
                self._root = x
            elif y == y.parent_node().left_node():
                y.parent_node().set_left_node(x)
            else:
                y.parent_node().set_right_node(x)

            if y != z:
                z.set_data(y.data())

            return y
        else:
            return None

    def traversal(self, in_order=True, pre_order=False, post_order=False):
        result = list()
        if in_order:
            in_order_list = list()
            result.append(self.__in_order(self._root, in_order_list))
        else:
            result.append(None)

        if pre_order:
            pre_order_list = list()
            result.append(self.__pre_order(self._root, pre_order_list))
        else:
            result.append(None)

        if post_order:
            post_order_list = list()
            result.append(self.__post_order(self._root, post_order_list))
        else:
            result.append(None)

        return result

    def __in_order(self, root, lista):
        if not root:
            return
        self.__in_order(root._left, lista)
        lista.append(root._data)
        self.__in_order(root._right, lista)
        return lista

    def __pre_order(self, root, lista):
        if not root:
            return
        lista.append(root._data)
        self.__pre_order(root._left, lista)
        self.__pre_order(root._right, lista)
        return lista

    def __post_order(self, root, lista):
        if not root:
            return
        self.__post_order(root._left, lista)
        self.__post_order(root._right, lista)
        lista.append(root._data)
        return lista

    def print_binary_tree(self):
        if self._root:
            print(self.traversal(False, True, False)[1])