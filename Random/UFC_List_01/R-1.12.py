'''
    R-1.12 O módulo random da linguagem Python possui a função choice(data) que
    retorna um elemento aleatório em uma sequência não vazia. O mesmo módulo inclui
    uma função mais básica randrange, com parametrização similar à função interna range,
    que retorna uma escolha aleatória dentro de um certo intervalo numérico. Utilizando
    apenas a função randrange, implemente a sua própria versão da função choice
'''

from random import randrange

def random_choice(*args: int) -> int or float:
    index = randrange(len(args))
    return args[index]

print(random_choice(80, 23, 12))