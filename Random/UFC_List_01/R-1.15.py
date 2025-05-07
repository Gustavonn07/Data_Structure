'''
    C-1.15 Escreva uma função Python que recebe uma sequência de números
    e determina se todos os números são diferentes uns dos outros.
'''

def is_repeated(*args) -> bool:
    num_set = set(args)
    return len(args) == len(num_set)

print(is_repeated(2, 3, 54, 6, 7))
print(is_repeated(2, 3, 54, 6, 7, 6))

