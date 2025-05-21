
# Dictionaries:
coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
print(coleta['Aedes aegypt'])

    # adiciona key e valor
coleta['Rhodnius montenegrensis'] = 11
print(coleta)
    # Deletar key em dict
del(coleta['Aedes albopictus'])
print(coleta)

print(coleta.items())
print(coleta.keys())
print(coleta.values())

print('-------')
coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
    # Atualiza os items de coleta add outros
coleta.update(coleta2)
print(coleta)

print('-------')
# Set (Conjuntos)
    # Elementos únicos: não aceita elementos repetidos.
    # Não ordenado: os elementos não têm uma ordem fixa.
    # Mutável: você pode adicionar ou remover elementos.
    # Não indexável: não dá para acessar um elemento pelo índice, como em listas.

    # retira os repetidos
biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo',
                'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')
print(set(biomoleculas))

a = {1, 2, 3}
b = {3, 4, 5}

    # União
print('---- Union ----')
print(a | b)
print(a.union(b))
    # Difference
print('---- Difference ----')
    # Elementos que estão em A e não em B
print(a - b)
print(a.difference(b))

print('---- Difference symmetric ----')
    # Elementos que estão em A ou em B, mas não em ambos
print(a ^ b)

print('---- Intersection ----')
    # Elementos que estão em ambos em A e em B
print(a & b)
print(a.intersection(b))




