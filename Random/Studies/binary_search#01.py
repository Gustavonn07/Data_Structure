
def binary_search(numbers_list: list[int], x: int):
    low = 0
    high = len(numbers_list) - 1

    while low <= high:
        mid = (high + low) // 2

        if numbers_list[mid] == x:
            return True, mid

        if numbers_list[mid] < x:
            low = mid + 1

        if numbers_list[mid] > x:
            high = mid - 1
    return False, None

# print(binary_search(list(range(1, 101)), 32))
print(binary_search(list(range(1, 101)), 32))
