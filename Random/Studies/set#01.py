"""
    Alunos em atividades extracurriculares
    Você recebeu os dados de alunos que participam de duas atividades na escola: futebol e xadrez.

    Crie dois conjuntos:
        Um com os nomes dos alunos que jogam futebol.
        Outro com os nomes dos alunos que jogam xadrez.

    Usando operações com ‘set’, responda:
        a) Quem participa das duas atividades?
        b) Quem participa apenas de futebol?
        c) Quem participa de pelo menos uma das duas?
        d) Quem participa somente de uma atividade?
"""

futebol = {"Ana", "Bruno", "Carlos", "Diana", "Edu"}
xadrez = {"Carlos", "Fernanda", "Edu", "Gabriel", "Helena"}

from enum import Enum

class SetEnum(Enum):
    INTERSSECTION = 1
    UNION = 2
    DIFFERENCE = 3
    SYMMETRIC_DIFFERENCE = 4

def get_set_type(enum: SetEnum):
    return {
        SetEnum.INTERSSECTION: '&',
        SetEnum.UNION: '|',
        SetEnum.DIFFERENCE: '-',
        SetEnum.SYMMETRIC_DIFFERENCE: '^',
    }[enum]

def get_group(enum: SetEnum):
    return eval(f"futebol {get_set_type(enum)} xadrez")

print(f'a) {get_group(SetEnum.INTERSSECTION)} participam das duas atividades')
print(f'b) {get_group(SetEnum.DIFFERENCE)} participam apenas de futebol')
print(f'c) {get_group(SetEnum.UNION)} participam de pelo menos uma atividade')
print(f'd) {get_group(SetEnum.SYMMETRIC_DIFFERENCE)} participam de somente uma atividade')

