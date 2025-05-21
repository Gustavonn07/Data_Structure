matriz = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

print(matriz)
# Não funciona por não ser uma matriz do numpy
# print(matriz.shape)

import numpy as np

matriz_np = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

print(matriz_np.shape)
print(matriz_np[0][2])
print('---------')

for i in matriz_np:
    for j in i:
        print(j, end=' ')