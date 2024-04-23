# Bug: Fails with empty list
def average(numbers: list[int]) -> float:
    """
    Get the average of a list of integers

    :param numbers: List of integers
    :returns: Float representing the average of those numbers
    """
    # Assumes the list is non-empty.
    return sum(numbers) / len(numbers)


# Bug: Assumes that words can't be over 100 chars in length
def contains_an_a(word: str) -> bool:
    """
    Checks whether a given string contains an "a" character

    :param word: The word/string to check for an "a"
    :returns: T/F about whether an "a" was found
    """
    for i in range(100):
        if i < len(word) and word[i] == "a":
            return True

    return False


# Bug: misses a case
def triangle_type(a: int, b: int, c: int) -> str:
    """
    Determine the type of a triangle based on the length of three sides

    :param a: Length of side a
    :param b: Length of side b
    :param c: Length of side c
    :returns: The type of triangle: Scalene, Equilateral, or Isosceles
    """

    if a == b == c:
        return "Equilateral"
    if a == b or b == c:
        return "Isosceles"
    else:
        return "Scalene"


def categorize_grade(grade: int) -> str:
    """
    Translate a number grade to a letter grade

    :param grade: The current grade of the student as an integer
    :returns: The string letter grade (e.g., "C+")
    """
    # Categorizes numerical grades into letter grades but has a logical error due to the use of else.
    letter_grade = ""
    if grade >= 97:
        letter_grade = "A+"
    if grade >= 93:
        letter_grade = "A"
    elif grade >= 90:
        letter_grade = "A-"
    elif grade >= 87:
        letter_grade = "B+"
    elif grade >= 83:
        letter_grade = "B"
    elif grade >= 80:
        letter_grade = "B-"
    elif grade >= 77:
        letter_grade = "C+"
    elif grade >= 73:
        letter_grade = "C"
    elif grade >= 70:
        letter_grade = "C-"
    elif grade >= 67:
        letter_grade = "D+"
    elif grade >= 63:
        letter_grade = "D"
    elif grade >= 60:
        letter_grade = "D-"
    else:
        letter_grade = "F"

    return letter_grade


# Bug: Returns true if the the first letters are the same
def is_palindrome(word: str) -> bool:
    """
    Checks whether a given word is a palindrome or not

    :param word: The word to check for palindromeness
    :returns: T/F of whether the word is a palindrome
    """
    for i in range(len(word) // 2):
        if word[i] == word[-1 + -i]:
            return True

    return False
