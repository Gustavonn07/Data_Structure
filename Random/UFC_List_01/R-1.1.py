'''
    R-1.1 Escreva a função Python is multiple(n, m) que recebe dois valores inteiros e
    retorna True se n for múltiplo de m, ou seja, se n = mi para um inteiro i, e False caso
    contrário.
'''

def is_multiple(n, m):
    return n % m == 0

print(is_multiple(100, 22))
print(is_multiple(100, 10))
