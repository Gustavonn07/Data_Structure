
def count_odd_or_pair[int](c: list[int], odd: int = 0, even: int = 0) -> bool:
    if not c:
        return odd > even

    if c[0] % 2 == 0:
        return count_odd_or_pair(c[1:], odd, even + 1)

    if c[0] % 2 != 0:
        return count_odd_or_pair(c[1:], odd + 1, even)

    return count_odd_or_pair(c[1:], odd, even)

print(count_odd_or_pair([12, 33, 44, 57]))  # True (ímpares: 2, pares: 2, no caso retorna False)
print(count_odd_or_pair([11, 13, 15]))      # True (3 ímpares, 0 pares)
print(count_odd_or_pair([22, 44, 68]))      # False (0 ímpares, 3 pares)
