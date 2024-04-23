def average(numbers: list[int]) -> float:
    """
    Get the average of a list of integers

    Bug: Assumes the list is non-empty

    :param numbers: List of integers
    :returns: Float representing the average of those numbers
    """
    return sum(numbers) / len(numbers)


def contains_an_a(word: str) -> bool:
    """
    Checks whether a given string contains an "a" character

    Bug: Assumes that words can't be over 100 chars in length

    :param word: The word/string to check for an "a"
    :returns: T/F about whether an "a" was found
    """
    for i in range(100):
        if i < len(word) and word[i] == "a":
            return True

    return False


def triangle_type(a: int, b: int, c: int) -> str:
    """
    Determine the type of a triangle based on the length of three sides

    Bug: Misses a case where `c == a`

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

    Bug: Logic error due to an `elif` being mistyped as an `if`

    :param grade: The current grade of the student as an integer
    :returns: The string letter grade (e.g., "C+")
    """
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


def is_palindrome(word: str) -> bool:
    """
    Checks whether a given word is a palindrome or not

    Bug: Only checks whether the first letters are the same

    :param word: The word to check for palindrome-ness
    :returns: T/F of whether the word is a palindrome
    """
    for i in range(len(word) // 2):
        if word[i] == word[-1 + -i]:
            return True

    return False
