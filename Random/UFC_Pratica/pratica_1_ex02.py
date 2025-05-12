from random import randint
from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insert(self, indice, elemento):
        """Insere na posição <indice> o valor <elemento>.
        Como se trata de uma lista, deve ser graratido que
        se houver valor em <indice> que ele não seja apagado"""
        ...

    @abstractmethod
    def remove(self, elemento):
        """Remove primeira ocorrência de <elemento>"""
        ...

    @abstractmethod
    def count(self, elemento):
        """Conta a quantidade de <elemento> na lista"""
        ...

    @abstractmethod
    def clear(self):
        """Apaga a lista"""
        ...

    @abstractmethod
    def index(self, elemento):
        """Retorna o primeiro índice de <elemento>"""
        ...

    @abstractmethod
    def length(self):
        """Retorna o tamanho da lista"""
        ...

    @abstractmethod
    def remove_all(self, item):
        """Remove todas as ocorrências de <item>"""
        ...

    @abstractmethod
    def remove_at(self, index):
        """Remove o elemento na posição <index>"""
        ...

    @abstractmethod
    def append(self, item):
        """Adiciona <item> ao final da lista - Concatenação"""
        ...

    @abstractmethod
    def replace(self, index, item):
        """Substitui o elemento na posição <index> por <item>"""
        ...


class Jogo:

    def __init__(self, ursos, peixes, num_rodadas):
        self.__ecossistema = Rio(ursos, peixes)
        self.__num_rodadas = num_rodadas

    def run(self):
        print(self.__ecossistema)
        for x in range(self.__num_rodadas):
            self.__ecossistema.rodada()
            print(self.__ecossistema)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# Duplamente Encadeada
class Rio:
    def __init__(self, qtd_ursos: int, qtd_peixes: int):
        self.head = None
        self.__popular_rio(qtd_ursos, qtd_peixes)

    def __popular_rio(self, qtd_ursos, qtd_peixes):
        self.__posicionar(Urso, qtd_ursos)
        self.__posicionar(Peixe, qtd_peixes)

    def __posicionar(self, classe, qtd: int):
        count = qtd
        while 0 < count:
            novo_node = Node(classe())
            novo_node.next = self.head
            if self.head:
                self.head.previous = novo_node
            self.head = novo_node
            count -= 1

    ''' 
        def __posicionar(self, classe, qtd: int):
                """Posicionar até qtd animais no rio"""
                count = qtd
                while 0 < count <= self.__rio.count(None):
                    for _ in range(qtd):
                        posicao = randint(0, len(self.__rio) - 1)
                        while self.__rio[posicao] is not None:
                            posicao = randint(0, len(self.__rio) - 1)
                        self.__rio[posicao] = classe()
                        count -= 1
    '''

    def __tamanho(self):
        count = 0
        actual = self.head
        while actual:
            count += 1
            actual = actual.next
        return count

    def rodada(self):
        count = 0
        actual = self.head
        while actual:
            direcao = randint(-1, 1)
            nova_pos = (count + direcao) % self.__tamanho()
            if nova_pos != count:
                self.__colisao(count, nova_pos)
            actual = actual.next

    '''
        def rodada(self):
            for x in range(len(self.__rio)):
                if self.__rio[x] is not None:
                    direcao = randint(-1, 1)
                    nova_posicao = (x + direcao) % len(self.__rio)
                    if nova_posicao != x:
                        self.__colisao(x, nova_posicao)
    '''

    def __procurar(self, index):
        count = 0
        actual = self.head
        while actual:
            if count == index:
                return actual.value
            count += 1
            actual = actual.next


    def __trocar(self, index, elemento):
        actual = self.head
        count = 0
        while actual:
            if count == index:
                if actual.previous:
                    actual.previous.next = actual.next
                else:
                    self.head = actual.next
                return elemento
            actual = actual.next
            count += 1

    def __colisao(self, posicao_atual, nova_posicao):
        animal_atual = self.__procurar(posicao_atual)
        animal_novo = self.__procurar(nova_posicao)

        acao = animal_atual.interagir(animal_novo)
        if acao == "comer":
            self.__trocar(nova_posicao, animal_atual)
            self.__trocar(posicao_atual, None)
        elif acao == "morrer":
            self.__trocar(posicao_atual, None)
        elif acao == "reproduzir":
            self.__posicionar(type(animal_atual), 1)
        elif acao == "mover":
            self.__trocar(nova_posicao, animal_atual)
            self.__trocar(posicao_atual, None)

    '''
        def __colisao(self, posicao_atual, nova_posicao):
            animal_atual = self.__rio[posicao_atual]
            animal_novo = self.__rio[nova_posicao]

            acao = animal_atual.interagir(animal_novo)
            if acao == "comer":
                self.__rio[nova_posicao] = animal_atual
                self.__rio[posicao_atual] = None
            elif acao == "morrer":
                self.__rio[posicao_atual] = None
            elif acao == "reproduzir":
                self.__posicionar(type(animal_atual), 1)
            elif acao == "mover":
                self.__rio[nova_posicao] = animal_atual
                self.__rio[posicao_atual] = None
    '''

    def __rio(self):
        rio = []
        actual = self.head
        while actual:
            rio.append(actual.value)
            actual = actual.next
        return rio

    def __str__(self):
        return "|".join(str(animal) if animal else " " for animal in self.__rio())


class Animal(ABC):
    @abstractmethod
    def interagir(self, outro) -> str:
        """Define a interação entre dois animais. Possíveis ações:
        - "comer": o animal come o outro
        - "morrer": o animal morre
        - "reproduzir": o animal se reproduz"""
        ...


class Urso(Animal):
    def interagir(self, outro):
        if outro:
            if isinstance(outro, Peixe):
                return "comer"
            elif isinstance(outro, Urso):
                return "reproduzir"
        return "mover"

    def __str__(self):
        return "🐻"


class Peixe(Animal):
    def interagir(self, outro):
        if outro:
            if isinstance(outro, Urso):
                return "morrer"
            elif isinstance(outro, Peixe):
                return "reproduzir"
        return "mover"

    def __str__(self):
        return "🐟"


if __name__ == '__main__':
    jogo = Jogo(3, 3, 5)
    jogo.run()
