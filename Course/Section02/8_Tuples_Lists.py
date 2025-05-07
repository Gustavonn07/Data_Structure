
# Tuplas
family_tuple = ('Gustavo', 'Fernanda', 'Peraltinha')
family_tuple2 = ('Gustavo2', 'Fernanda2', 'Peraltinha2')
print(family_tuple[-1])

print(family_tuple2 + family_tuple)

print(family_tuple.index('Gustavo'))

for name in family_tuple:
    print(name)

print('-------------------')

# Listas
grades_this_year = [0, 9.4, 2.2, 7.4]
grades_last_year = [1, 7, 6.6, 9.1]

print(grades_this_year + grades_last_year)
print(grades_this_year * 2)
print(grades_this_year[0:2])

grades_this_year.append(2.1)
print(grades_this_year)

grades_this_year.remove(2.1)
print(grades_this_year)
