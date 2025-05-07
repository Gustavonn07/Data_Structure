'''
    Escreva a função Python minmax(data) que recebe uma sequência de um ou
    mais núumeros e retorna o menor e o maior números da lista na forma de uma tupla
    de tamanho dois. Você não pode utilizar as funções min e max do Python (built-in
    functions) na implementação de sua solução.
'''

def minmax(*data):
    if not data:
        raise ValueError('É necessário passar valores válidos')

    min_value = None
    max_value = None
    for item in data:
        if min_value is None or min_value > item:
            min_value = item
        if max_value is None or max_value < item:
            max_value = item

    return min_value, max_value

print(minmax(92, -3, 12, -55, 99, 21, 54, 102))
