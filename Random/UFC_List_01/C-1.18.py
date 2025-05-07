'''
    C-1.18 Mostre como utilizar a sintaxe Python de compreensão de lista para gerar a
    lista [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
'''

# 2, 4, 6, 8, 10,...
def get_list() -> list[int]:
    return [sum([j * 2 for j in range(i)]) for i in range(1, 11)]

print(get_list())