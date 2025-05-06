'''
    Leia a idade do usuário e classifique-o em:
    - Criança – 0 a 12 anos
    - Adolescente – 13 a 17 anos
    - Adulto – acima de 18 anos
    -Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida
'''
from enum import Enum

class Classification(Enum):
    CHILD = 1
    ADOLESCENT = 2
    ADULT = 3

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def _get_classification_type(self):
        if self._age < 0:
            return None

        if self._age <= 12:
            return Classification.CHILD

        if self._age <= 17:
            return Classification.ADOLESCENT

        return Classification.ADULT

    def get_classification(self) -> str:
        classification = self._get_classification_type()

        if classification is None:
            return 'Tipo Inválido'

        texts = {
            Classification.CHILD: 'Criança',
            Classification.ADOLESCENT: 'Adolescente',
            Classification.ADULT: 'Adulto'
        }
        return texts[classification]

person0 = Person('Felipe', 11)
person1 = Person('Luis', 16)
person2 = Person('Mara', 32)
person3 = Person('#@$#$', -213)

print(person0.get_classification())
print(person1.get_classification())
print(person2.get_classification())
print(person3.get_classification())

# FAZER ISSO
'''
    Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3;
    passando por um cálculo da média aritmética. 
    Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
    - Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
    - Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
    - Se a média for maior do que 6.0, o aluno está aprovado
    - Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
'''

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def say_name(self) -> str:
        return self._name

class Media(Enum):
    FAILED = 1
    EXAM = 2
    PASS = 3

class Student(Person):
    def __init__(self, name: str, age: int, m1: float, m2: float, m3: float):
        super().__init__(name, age)
        self._m1 = m1
        self._m2 = m2
        self._m3 = m3

    def _get_media_value(self) -> float:
        return (self._m1 + self._m2 + self._m3) / 3

    def _get_media_classification(self):
        media = self._get_media_value()
        if media <= 4.0: return Media.FAILED
        if media <= 6.0: return Media.EXAM
        if media > 6.0: return Media.PASS
        return None

    def get_result(self) -> str or None:
        classification = self._get_media_classification()
        if classification is None: return None
        texts = {
            Media.FAILED: 'Reprovado',
            Media.EXAM: 'Em Exame',
            Media.PASS: 'Aprovado',
        }
        return texts[classification]

p1 = Student('Jorge', 20, 7.0, 5.5, 6.5)
print(p1.get_result())
