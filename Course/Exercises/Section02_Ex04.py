'''
    Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene numa lista.
    Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados
'''

from random import randint

list_numbers = []
for i in range(5):
    list_numbers.append(randint(0, 100))

c = 0
for n in list_numbers:
    c += n

print(f'R01: Valor somado -> {c} \n Lista -> {list_numbers}')



'''
    Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, 
    fazendo a leitura dos valores por meio de uma estrutura de repetição. 
    Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
'''

dict_classroom = {
    'Peralta': 9.8,
    'Fernanda': 10,
    'Gustavo': 0.8
}

c = 0
for i in dict_classroom:
    c += dict_classroom[i]

print(f'R02: Média -> {(c / 3):.2f}')



'''
    Matriz: Dada a matriz abaixo, 
    construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

    matriz = np.array([
        [3, 4, 1],
        [3, 1, 5]
    ])
'''

import numpy as np

matriz = np.array([
        [3, 4, 1],
        [3, 1, 5]
    ])

c = 0
for i in matriz:
    for j in i:
        c += j

print(f'R03: Soma -> {c}')