'''
🛠️ Funções principais que uma árvore binária geralmente tem:
    Função __//__ O que faz:

    insert(value) __//__ Insere um valor na árvore ✅
    search(value) __//__ Verifica se um valor existe na árvore ✅
    delete(value) __//__ Remove um valor da árvore (se quiser implementar isso)
    find_min() __//__ Encontra o menor valor (útil em árvores de busca)
    find_max() __//__ Encontra o maior valor

    inorder() __//__ Percorre em ordem (esquerda → raiz → direita)
    preorder() __//__ Percorre em pré-ordem (raiz → esquerda → direita)
    postorder() __//__ Percorre em pós-ordem (esquerda → direita → raiz)
'''



class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    def empty(self):
        return self._data is None

    def get_data(self):
        return self._data

    def set_parent(self, parent):
        self._parent = parent

    def get_left_child(self):
        return self._left

    def set_left_child(self, children):
        self._left = children

    def get_right_child(self):
        return self._right

    def set_right_child(self, children):
        self._right = children

    def has_left_child(self):
        if self._left:
            return True
        else:
            return False

    def has_right_child(self):
        if self._right:
            return True
        else:
            return False

class BinaryTree:
    def __init__(self, data):
        if not data:
            raise ValueError('Data deve ser informada')
        self._root = Node(data)
        self._qtd_nodes = 1

    def empty(self):
        return self._root.empty() is None

    def search(self, data):
        if self._root is None:
            return False
        else:
           return self.__find_children(self._root, data)

    def __find_children(self, parent, data):
        if not parent:
            return False
        elif parent.get_data() == data:
            return True
        elif parent.get_data() < data:
            return self.__find_children(parent.get_right_child(), data)
        else:
            return self.__find_children(parent.get_left_child(), data)


    def insert(self, node):
        if self.empty():
            self._root = node
            return self._root
        else:
            self._qtd_nodes += 1
            return self._insert_children(self._root, node)

    def _insert_children(self, parent, children):
        if parent.get_data() > children.get_data():
            if not parent.has_left_child():
                parent.set_left_child(children)
                children.set_parent(parent)
            else:
                self._insert_children(parent.get_left_child(), children)
        else:
            if not parent.has_right_child():
                parent.set_right_child(children)
                children.set_parent(parent)
            else:
                self._insert_children(parent.get_right_child(), children)


if __name__ == "__main__":
    arvore = BinaryTree(10)
    arvore.insert(Node(5))
    arvore.insert(Node(15))
    arvore.insert(Node(7))
    arvore.insert(Node(3))

    def inorder(node):
        if node:
            inorder(node.get_left_child())
            print(node.get_data(), end=' ')
            inorder(node.get_right_child())

    inorder(arvore._root)

    resultado = arvore.search(15)
    print("Encontrado:", resultado)
    resultado = arvore.search(19)
    print("Encontrado:", resultado)

