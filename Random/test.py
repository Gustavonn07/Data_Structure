from unittest import TestCase


"""Neste arquivo você encontra implementada uma árvore binária.
Uma árvore binária é uma estrutura de dados onde cada nó tem no máximo dois filhos,
chamados de filho esquerdo e filho direito. Neste tipo de árvore, não existe
uma ordenação específica entre os valores dos nós filhos.
"""




# Nó que armazena um valor e referências para os filhos e pai
class BinaryTreeNode:
    def _init_(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent




# Árvore binária que permite inserção e busca de valores
class BinaryTree:
    def _init_(self, value):
        self.root = BinaryTreeNode(value)


    def insert(self, value):
        self.__insert_recursive(self.root, value)


    def __insert_recursive(self, node, value):
        if node.left is None:
            node.left = BinaryTreeNode(value, parent=node)
            return True
        elif node.right is None:
            node.right = BinaryTreeNode(value, parent=node)
            return True, node.right
        else:
            if self.__insert_recursive(node.left, value):
                return True
            return self.__insert_recursive(node.right, value)


    def search(self, value, node=None):
        if node is None:
            node = self.root


        if self.is_valid_BST():
            # Busca binária (otimizada)
            if node is None:
                return None
            if node.value == value:
                return node
            elif value < node.value:
                return self.search(value, node.left)
            else:
                return self.search(value, node.right)
        else:
            # Busca completa (não otimizada)
            if node is None:
                return None
            if node.value == value:
                return node
            found = None
            if node.left:
                found = self.search(value, node.left)
            if not found and node.right:
                found = self.search(value, node.right)
            return found




    def is_valid_BST(self):
        def validate(node, min_value, max_value):
            if node is None:
                return True
            if not (min_value < node.value < max_value):
                return False
            return (validate(node.left, min_value, node.value) and
                    validate(node.right, node.value, max_value))


        return validate(self.root, float('-inf'), float('inf'))






class TestBinaryTree(TestCase):


    def setUp(self):
        self.tree1 = BinaryTree(10)
        self.tree1.insert(5)
        self.tree1.insert(15)
        self.tree1.insert(3)


        self.tree2 = BinaryTree(10)
        self.tree2.insert(15)
        self.tree2.insert(5)
        self.tree2.insert(20)
        self.tree2.insert(14)


    def test_is_valid_BST(self):
        self.assertTrue(self.tree1.is_valid_BST())
        self.assertFalse(self.tree2.is_valid_BST())


"""
Justificativa:
Quando a árvore é uma árvore de busca binária (BST), a gente consegue
usar a ordenação para descartar metade da árvore a cada comparação, o que
deixa a busca com complexidade média de O(log n). Por outro lado, numa árvore
binária sem ordenação, é preciso percorrer todos os nós no pior caso, ficando O(n).
Por isso, faz sentido verificar se é uma BST antes de buscar, já que isso pode
melhorar o desempenho quando a árvore estiver organizada.
"""