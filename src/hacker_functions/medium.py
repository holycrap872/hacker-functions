# Bug: Fails when s is either empty
def capitalize_first(s: str) -> str:
    return s[0].upper() + s[1:]


# Bug: bug occurs b/c doesn't handle <=
def find_middle(a: int, b: int, c: int) -> int:
    if a < b < c:
        return b
    elif a < c < b:
        return c
    elif b < c < a:
        return c
    elif b < a < c:
        return a
    elif c < a < b:
        return a
    else:
        return b


# Bug: Off by one error
def count_matches(l: list[str], word: str):
    matches = 0
    for i in range(len(l) - 1):
        if l[i] == word:
            matches += 1
    return matches


# Bug: Function returns False too early
def find_in_list(lst: list[int], item: int) -> bool:
    for i in lst:
        if i == item:
            return True
        elif i > item:
            return False
    return False


# Bug: Assumes the strings are of equal length
def strings_equal(s1: str, s2: str) -> bool:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


# Bug: The function assumes the list is always non-empty
def max_number(numbers: list[int]) -> int:
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num
