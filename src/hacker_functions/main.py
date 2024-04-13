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


# Bug: Off by one error
def count_matches(l: list[str], word: str):
    matches = 0
    for i in range(len(l) - 1):
        if l[i] == word:
            matches += 1
    return matches


# Bug: Fails when s is either empty
def capitalize_first(s: str) -> str:
    return s[0].upper() + s[1:]


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


def run_command(command: str, *, is_admin: bool) -> str:
    admin_only = ["remove", "download", "create"]
    if not is_admin:
        for c in admin_only:
            if c == command or c.upper() == command:
                return "Sorry, that's only for admin"

    return f"Executed command {command.lower()}"


# Bug: Fails to check for the position of . which should be after @
def is_valid_email(email: str) -> bool:
    # Checks if an email is valid based on simplistic criteria.
    return "@" in email and "." in email.split("@")[1]


# Bug: The function fails for negative numbers due to the negative sign.
def sum_of_digits(n: int) -> int:
    # Returns the sum of the digits in the integer n.
    return sum(int(char) for char in str(n))


# Bug: Fails to handle cases where currency is not in rates dictionary
def convert_to_usd(amount: int, currency: str) -> float:
    # Converts an amount from a specified currency to USD.
    rates = {"EUR": 1.1, "JPY": 0.0091}
    return amount * rates[currency]


def authenticate(password: str) -> bool:
    # Mimics a buffer overflow vulnerability - a classic error in languages like C
    buffer = [""] * 10
    for i in range(len(password)):
        buffer[i] = password[i]
    return buffer == ["s", "e", "c", "r", "e", "t", "", "", "", ""]


# Bug: Off-by-one error that manifests only if the list length is odd
def pair_items_in_list(items: list[int]) -> list[tuple[int, int]]:
    processed = []

    i = 0
    while i < len(items) - 1:
        # Processes in pairs
        processed.append((items[i], items[i + 1]))
        i += 2

    return processed


# Bug: Incorrect for even-length lists
def find_median(numbers: list[int]) -> int:
    sorted_numbers = sorted(numbers)
    return sorted_numbers[len(sorted_numbers) // 2]
