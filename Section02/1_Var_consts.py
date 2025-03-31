#Variáveis e constantes
#Por meio de variáveis que um algortimo “guarda” os dados do problema
#Todo dado que tem a possibilidade de ser alterado no decorrer do tempo deverá ser tratado como uma variável
#Quando um dado não tem nenhuma possibilidade de variar no decorrer do tempo, deverá ser tratado como constante
#Exemplo: calcular a área de um triângulo. Sabemos que a fórmula para o cálculo da área de um triângulo é BASE * ALTURA / #2. Base e altura são dados que irão variar no decorrer do “tempo de execução”. O número 2 da fórmula é um dado #constante, pois sempre terá o mesmo valor

#Tipo de variáveis
#Inteiros: valores positivos ou negativos, que não possuem uma parte fracionária. Exemplos: 1, 30, 40, 12, -50
#Float (real): valores positivos ou negativos, que podem possuir uma parte fracionária (também podem ser inteiros). #Exemplos: 1.4, 6.7, 10.3, 100, -47
#Caracteres (char ou string): qualquer elemento presente no teclado. Exemplos: “Maria”, “João”, ‘M’, ‘F’
#Lógico (boleano): verdadeiro ou falso. Exemplos: true, false, 1, 0


numero = -1
numero_jogos = 14
numeros_float = 1.4
# Numeros tipo int && float
print(numero, numero_jogos, numeros_float)

str = 'olá mundo!'
char = 'a'
# Strings tipo string && char
print(str, char)
# formatt
print(f'{str} não possui {char}')

boolean_true = True
boolean_false = False

if(boolean_false):
    nome = input('Insira seu nome: ')
    if (nome):
        print(f'Nome: {nome}')
    else:
        print(boolean_false)
