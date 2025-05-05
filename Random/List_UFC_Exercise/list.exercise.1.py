'''
    1 - Utilizando as implementações de listas que vimos em sala de aula (listas simples e
    duplamente encadeadas, disponibilizadas no arquivo lists.py), implemente os seguintes
    métodos
    • length(self), que retorna o tamanho da lista;
    • remove_all(self, item), que remove todas as ocorrências de item;
    • remove_at(self, index), que remove o item na posição index;
    • append(self, item), que concatena item na lista;
    • replace(self, index, item), que substitui o que se encontra na lista na
    posição index por item.
    Lembre-se de modificar a especificação de ListADT de modo obrigar que as classes
    LinkedList e DoublyLinkedList sejam obrigadas e implementar tais métodos.
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


class LinkedList(ListADT):
    class Node:
        def __init__(self, elemento):
            self.elemento = elemento
            self.proximo = None

    def __init__(self):
        self.head = None
        self._size = 0

    def insert(self, indice, elemento):
        if indice < 0 | indice > self._size:
            raise IndexError("Índice fora do intervalo")

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

lista = LinkedList()
lista.insert(0, 10)
lista.insert(1, 20)
lista.insert(2, 15)

# Teste de length
print(f"Tamanho da lista: {lista.length()}")

# Teste de remove_at
lista.remove_at(0)
print(f"Tamanho da lista: {lista.length()}")

# Teste de remove_all
lista.remove_all()
print(f"Tamanho da lista: {lista.length()}")
try:
    print(f"Testar valor de index excluído: {lista.index(10)}")
except ValueError as e:
    print(f"Erro ao buscar índice: {e}")

# Teste do append
lista.append(23)
lista.append(33)
lista.append(43)
print(f"Tamanho da lista: {lista.length()}")
print(lista.index(33))

# Teste de replace
lista.replace(1, 77)
print(lista.index(77))
