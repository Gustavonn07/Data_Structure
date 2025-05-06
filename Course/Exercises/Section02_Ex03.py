# Ler 5 notas e informar a média
from random import randint

media = 0
for num in range(0, 5):
    random_n = randint(0, 11)
    media += random_n
    if num == 4:
        print(media / 5)


# Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
loop = 0
while loop < 10:
    loop += 1
    print(f'3 x {loop} = {3 * loop}')