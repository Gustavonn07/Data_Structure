'''
    R-1.4 Escreva uma função Python que recebe um inteiro positivo n e retorna a
    soma dos quadrados de todos os inteiros positivos menores que n.
'''

def multiplication_smaller_numbers(number: int) -> float or int:
    acc = 0
    for number_counter in range(1, number):
        acc += number_counter**2

    return acc

print(multiplication_smaller_numbers(5))
