'''
    P-1.34: Uma punição comum em escolas é fazer com que uma criança escreva uma determinada frase várias vezes.
    Escreva um programa Python capaz de escrever a seguinte frase cem vezes: “Eu nunca mais vou enviar spam para meus amigos novamente.”.
    Seu programa deve, ainda, numerar todas as frases escritas e fazer oito erros diferentes de escrita, todos aparentemente aleatórios.
    (Nota do tradutor: a punição é bastante boba e pouco educativa, mas a intenção é colocar em prática os conhecimentos de programação.)
'''

# Repetir 100x -OK
# Numerar as frases -OK
# 8 erros de escrita (no total)

from random import randint, choice

def repeat_100(string: str) -> None:
    errors = 8
    errors_indexes = []
    letras_validas = [c for c in string if c.isalpha()]
    for index in range(errors):
        errors_indexes.append(randint(0, 100))

    for n in range(100):
        if n in errors_indexes:
            print(f'Nº{n + 1} {string.replace(choice(letras_validas), '', 1)}')
        else:
            print(f'Nº{n + 1} {string}')

repeat_100('Eu nunca mais vou enviar spam para meus amigos novamente.')
