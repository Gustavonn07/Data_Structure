'''
    R-1.5 Baseando-se na sintaxe Python de compreensão de lista e na função interna
    sum, escreva um comando único que computa a soma do exercício R-1.4
'''

def sum_of_squares(number: int) -> int or float:
    return [item**2 for item in range(1, number)]

print(sum_of_squares(5))
