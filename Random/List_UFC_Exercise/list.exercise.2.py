'''
    2 - Utilizando as implementações de LinkedList ou DoublyLinkedList (você pode
    escolher o que achar mais adequado), implemente uma lista chamada NoDupsList. Nessa
    lista, todos os métodos de ListADT devem ser implementados. A única modificação é que
    o método insert não pode inserir um valor caso ele já exista na lista. Na tentativa de
    inserção de um valor que já existe na lista, o método deve lançar uma exceção. Trata-se,
    portanto, de uma lista que garante que não conterá valores duplicados.
'''

from abc import ABC, abstractmethod

class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """
            Insere na posição <indice> o valor <elemento>, será automaticamente feita a disposição de nós com o seu
            ponteiro funcional para o próximo nó.
        """
        pass

    @abstractmethod
    def remove_at(self, elemento):
        """Remove a primeira ocorrência de <elemento>. Substituindo o próprio pelo valor anterior"""
        pass

    @abstractmethod
    def replace(self, indice, elemento):
        """Remove a primeira ocorrência de <indice>. Substituindo o valor de <elemento>"""
        pass

    @abstractmethod
    def count(self, elemento):
        """Conta a quantidade de <elemento> na lista."""
        pass

    @abstractmethod
    def remove_all(self):
        """Apaga a lista."""
        pass

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro índice de <elemento>."""
        pass

    @abstractmethod
    def length(self):
        """Retorna o tamanho total da lista existente."""
        pass


class NoDupsList(ListADT):
    class Node:
        def __init__(self, elemento):
            self.elemento = elemento
            self.proximo = None

    def __init__(self):
        self.head = None
        self._size = 0

    def insert(self, indice, elemento):
        if indice < 0 or indice > self._size:
            raise IndexError("Índice fora do intervalo")

        atual = self.head
        while atual:
            if atual.elemento == elemento:
                raise ValueError(f"Elemento '{elemento}' já existe na lista")
            atual = atual.proximo

        novo_node = self.Node(elemento)

        if indice == 0:
            novo_node.proximo = self.head
            self.head = novo_node
        else:
            atual = self.head
            for _ in range(indice - 1):
                atual = atual.proximo
            novo_node.proximo = atual.proximo
            atual.proximo = novo_node

        self._size += 1

    def replace(self, indice, elemento):
        if indice < 0 or indice >= self._size:
            raise IndexError("Índice fora do intervalo")

        atual = self.head
        for _ in range(indice):
            atual = atual.proximo

        atual.elemento = elemento

    def append(self, elemento):
        novo_node = self.Node(elemento)
        if self.head is None:
            self.head = novo_node
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_node
        self._size += 1

    def remove_at(self, indice):
        if indice < 0 or indice >= self._size:
            raise IndexError("Índice fora do intervalo")

        if indice == 0:
            self.head = self.head.proximo
        else:
            atual = self.head
            for _ in range(indice - 1):
                atual = atual.proximo
            atual.proximo = atual.proximo.proximo

        self._size -= 1

    def count(self, elemento):
        atual = self.head
        contador = 0
        while atual:
            if atual.elemento == elemento:
                contador += 1
            atual = atual.proximo
        return contador

    def remove_all(self):
        self.head = None
        self._size = 0


    def index(self, elemento):
        atual = self.head
        indice = 0
        while atual:
            if atual.elemento == elemento:
                return indice
            indice += 1
            atual = atual.proximo
        raise ValueError(f"Elemento {elemento} não encontrado")

    def length(self):
        return self._size

lista = NoDupsList()
#Verificar erro de insert duplicado
lista.insert(0, 10)
lista.insert(1, 15)
lista.insert(2, 15)

