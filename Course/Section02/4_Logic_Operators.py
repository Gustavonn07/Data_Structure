value_true = True
value_false = False

print(value_true)
print(value_false)

print('--------------------')

print(value_true & value_false)
print(value_true | value_false)

print('--------------------')

print(value_true and value_false)
print(value_true or value_false)

print('--------------------')

print(not value_true)
print(not value_false)

print('--------------------')

# XOR
# Ele compara dois valores bit a bit, ou, no caso de booleanos (True/False), compara diretamente os valores lógicos.
# O resultado é True se apenas um dos valores for True.
# Se os dois forem iguais (True/True ou False/False), o resultado é False.
print(value_true ^ value_false)