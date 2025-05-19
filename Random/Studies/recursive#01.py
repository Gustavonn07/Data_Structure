
def min_max[T](numbers_list: list[T]) -> tuple[T, T]:
    if len(numbers_list) == 1:
        return numbers_list[0], numbers_list[0]

    if len(numbers_list) == 2:
        return min(numbers_list[0], numbers_list[1]), max(numbers_list[0], numbers_list[1])

    mid = len(numbers_list) // 2
    min1, max1 = min_max(numbers_list[mid:])
    min2, max2 = min_max(numbers_list[:mid])

    return min(min1, min2), max(max2, max2)

list1 = [1, 9, 8, 2, 3, 4, 5, 6, 7]
print(min_max(list1))