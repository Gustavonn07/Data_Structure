
def is_palin(word: str) -> bool:
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palin(word[1:-1])

print(is_palin("arara"))     # True
print(is_palin("radar"))     # True
print(is_palin("python"))    # False
print(is_palin("palaxrrexlap")) # False
