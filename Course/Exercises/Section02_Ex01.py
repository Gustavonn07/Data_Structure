#Olá!
from typing import Callable

# Para revisar o conteúdo prático visto até agora, você agora pode resolver dois exercícios. Logo em seguida você pode acessar a
# aula em vídeo com a solução

# Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

class Calculator:
    def __init__(self, num1: int, num2: int):
        self._num1 = num1
        self._num2 = num2

    def calculate(self, handler: Callable[[int, int], float] ):
        return print(f'Valor calculado: {handler(self._num1, self._num2)}')

calc = Calculator(10, 2)
calc.calculate(lambda num1, num2: num1 + num2)
calc.calculate(lambda num1, num2: num1 - num2)
calc.calculate(lambda num1, num2: num1 * num2)
calc.calculate(lambda num1, num2: num1 / num2)

# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma,
# será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância,
# basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12.
# O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros
# utilizada na viagem

time = 2
velocity = 120

def calculate_distance(time: int, velocity: int) -> int:
    return time * velocity

def calculate_used(distance: int):
    return distance / 12

print(calculate_used(calculate_distance(time, velocity)))