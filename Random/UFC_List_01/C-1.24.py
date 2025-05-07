'''
    C-1.24 Escreva uma função Python que conte o número de vogais em um determinado string
'''

def count_vowels(string: str) -> int:
    acc = 0
    for letter in string:
        if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
            acc += 1
    return acc

print(count_vowels('Era uma vez um pato'))
