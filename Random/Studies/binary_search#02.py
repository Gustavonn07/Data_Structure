
def binary_search_recursive(items, low, high, x):
    while low <= high:
        mid = (high + low) // 2

        if items[mid] == x:
            return True, mid

        if items[mid] > x:
            return binary_search_recursive(items, low, mid - 1, x)

        if items[mid] < x:
            return binary_search_recursive(items, mid + 1, high, x)
    return False, -1

print(binary_search_recursive(list(range(1, 101)), 0, 100, 32))