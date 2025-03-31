#Olá!

#Para revisar o conteúdo prático visto até agora, você agora pode resolver dois exercícios. Logo em seguida você pode acessar a aula em vídeo com a solução

#Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

#Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

#Bom trabalho,

#Jones

num1 = 10
num2 = 3

print(f'Soma: {num1 + num2}')
print(f'Subtração: {num1 - num2}')
print(f'Multiplicação: {num1 * num2}')
print(f'Divisão: {round(num1 / num2, 2)}')

def getLitrosUsados(tempo: int, velocidade: float, km_por_litro: float = 12) -> tuple[float, float]:
    distancia = tempo * velocidade
    litros_usados = distancia / km_por_litro
    return distancia, litros_usados

# Definição das variáveis
tempo_gasto = 20  # em horas
velocidade_media = 120  # em km/h

# Chamada da função
distancia, litros = getLitrosUsados(tempo_gasto, velocidade_media)

# Exibição dos resultados formatados
print(f'Velocidade média: {velocidade_media} km/h')
print(f'Tempo gasto na viagem: {tempo_gasto} horas')
print(f'Distância percorrida: {distancia} km')
print(f'Combustível gasto: {litros:.2f} litros')