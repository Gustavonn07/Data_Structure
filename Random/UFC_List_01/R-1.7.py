'''
    R-1.7 Baseando-se na sintaxe Python de compreensão de lista e na função interna
    sum, escreva um comando único que computa a soma do exercício R-1.6
'''

def get_odds_squares(n: int) -> int or float:
    return [x**2 for x in range(1, n) if x % 2 != 0]

print(get_odds_squares(5))