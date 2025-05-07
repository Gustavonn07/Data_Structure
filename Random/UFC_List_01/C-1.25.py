'''
    C-1.25 Escreva uma função Python que recebe um string, representando uma frase e
    retorna uma cópia desta frase com todas os sinais de pontuação removidos. Por exemplo,
    se o string ”Vamos tentar, Miguel.” for passado com parâmetro, a função deve retornar
    ”Vamos tentar Miguel”.
'''

import re

def clean_string(string: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', string)

print(clean_string('Testes,.#adasd//;;[2314'))
