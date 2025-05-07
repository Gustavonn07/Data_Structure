'''
    R-1.6 Escreve uma função Python que recebe um inteiro positivo n e retorna a som
    dos quadrados de todos os inteiros positivos ímpares menores que n.
'''

def sum_odds(n: int) -> int or float:
    acc = 0
    for item in range(1, n):
        if item % 2 != 0:
            acc += item**2

    return acc

print(sum_odds(5))
