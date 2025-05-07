'''
    C-1.26 Escreva um pequeno programa que recebe como entrada três inteiros no console (linha de comando)
    e determina se eles podem ser utilizados em fórmulas aritméticas
    (seguindo a ordem de entrada do usuário), como, por exemplo, a + b = c, a = b − c ou
    a ∗ b = c.
'''

def can_be_used(n1: int, n2: int, n3: int) -> bool:
    return (n1 + n2 == n3) or (n1 == n2 - n3) or (n1 * n2 == n3)

print(can_be_used(2, 3, 5))
print(can_be_used(10, 5, 5))
print(can_be_used(3, 3, 9))
print(can_be_used(1, 2, 4))