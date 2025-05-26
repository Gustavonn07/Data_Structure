"""
📌 O que é uma lista?
    É uma coleção ordenada e mutável de elementos.
    Você pode armazenar qualquer tipo de dado (números, ‘strings’, objetos, até outras listas).
"""

'''
📌 O que é uma lista encadeada?
    É uma estrutura onde cada elemento (nó) aponta para o próximo. Diferente das listas nativas do Python, 
    que são implementadas como arrays dinâmicos.
'''

from abc import ABC, abstractmethod

class AbstractChainList(ABC):

    @abstractmethod
    def insert(self, value): pass

    @abstractmethod
    def remove(self, value): pass

    @abstractmethod
    def search(self, value): pass

    @abstractmethod
    def exibe(self): pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ChainList(AbstractChainList):
    def __init__(self):
        self.head = None

    def insert(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove(self, value: str | float | int) -> None:
        actual = self.head
        previous = None
        while actual:
            if actual.value == value:
                if previous is None:
                    self.head = actual.next
                else:
                    previous.next = actual.next
                return
            previous = actual
            actual = actual.next

    def search(self, value: str | float | int) -> str | float | int | None:
        actual = self.head
        while actual:
            if actual.value == value:
                return actual.value
            actual = actual.next
        return None

    def exibe(self) -> None:
        if not self.head:
            print("Lista vazia")
            return

        actual = self.head
        while actual:
            print(actual.value, end=" -> ")
            actual = actual.next
        print('None')

# Teste
chained_list = ChainList()
chained_list.insert(10)
chained_list.insert(12)
chained_list.insert(15)
chained_list.exibe()        # 15 -> 12 -> 10 -> None
chained_list.remove(12)
chained_list.exibe()        # 15 -> 10 -> None
print(chained_list.search(10))  # 10
print(chained_list.search(12))  # None