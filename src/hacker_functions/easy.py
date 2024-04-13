# Bug: Fails with empty list
def average(numbers: list[int]) -> float:
    # Assumes the list is non-empty.
    return sum(numbers) / len(numbers)


# Bug: Assumes that words can't be over 100 chars in length
def contains_an_a(word: str) -> bool:
    for i in range(100):
        if i < len(word) and word[i] == "a":
            return True

    return False


# Bug: misses a case
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    if a == b or b == c:
        return "Isosceles"
    else:
        return "Scalene"


def categorize_grade(grade):
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
def palindrome_checker(word: str) -> bool:
    for i in range(len(word) // 2):
        if word[i] == word[-1 + -i]:
            return True

    return False
