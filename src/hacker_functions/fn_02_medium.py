# Bug: Fails when s is either empty
def capitalize_first(s: str) -> str:
    """
    Capitalize the first letter of a word/sentence

    :param s: The word/sentence to capitalize
    :returns: The updated (capitalized) string
    """
    return s[0].upper() + s[1:]


# Bug: bug occurs b/c doesn't handle <=
def find_middle(a: int, b: int, c: int) -> int:
    """
    Find the second largest of three numbers. For example, given the inputs
    (3, 6, 5), the function would return 5 since it's the second largest -
    middle number.

    :param a: First integer
    :param b: Second integer
    :param c: Third integer
    :returns: The middle - second largest - number
    """
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
def count_matches(l: list[str], word: str) -> int:
    """
    Count the number of times a given word appears in a list of words

    :param l: The list of strings/words
    :param word: The word to look for matches for
    """
    matches = 0
    for i in range(len(l) - 1):
        if l[i] == word:
            matches += 1
    return matches


# Bug: Function returns False too early
def find_in_list(lst: list[int], item: int) -> bool:
    """
    Determines whether a given item appears in a list

    :param lst: A list of integers
    :param item: The item to look for in the list
    :returns: T/F about whether the item is in the list
    """
    for i in lst:
        if i == item:
            return True
        elif i > item:
            return False
    return False


# Bug: Assumes the strings are of equal length
def strings_are_equal(s1: str, s2: str) -> bool:
    """
    Determine whether two strings are equal

    :param s1: The first string
    :param s2: The second string
    :returns: T/F of whether the two strings are equal
    """
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


# Bug: The function assumes the list is always non-empty
def max_number(numbers: list[int]) -> int:
    """
    Find the largest number in a list of integers

    :param numbers: List of numbers
    :returns: The largest integer in the list of numbers
    """
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num
