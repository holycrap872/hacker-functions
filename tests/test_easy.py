import pytest

from hacker_functions.easy import average, categorize_grade, contains_an_a, palindrome_checker, triangle_type


def test_average_1() -> None:
    assert average([5, 6, 7]) == 6.0


def test_average_2() -> None:
    assert average([2, 2, 2]) == 2.0


# ZeroDivisionError
@pytest.mark.xfail
def test_average_3() -> None:
    assert average([])


def test_contains_a_1() -> None:
    assert contains_an_a("hello") == False


def test_contains_a_2() -> None:
    assert contains_an_a("halo") == True


# AssertionError
@pytest.mark.xfail
def test_contains_a_3() -> None:
    assert contains_an_a("b" * 1000 + "a") == True


def test_triangle_type_1() -> None:
    assert triangle_type(3, 3, 3) == "Equilateral"


def test_triangle_type_2() -> None:
    assert triangle_type(3, 3, 4) == "Isosceles"


def test_triangle_type_3() -> None:
    assert triangle_type(3, 4, 5) == "Scalene"


# AssertionError
@pytest.mark.xfail
def test_triangle_type_4() -> None:
    assert triangle_type(3, 4, 3) == "Isosceles"


def test_categorize_grade_1() -> None:
    assert categorize_grade(60) == "D-"


def test_categorize_grade_2() -> None:
    assert categorize_grade(95) == "A"


# AssetionError
@pytest.mark.xfail
def test_categorize_grade_3() -> None:
    assert categorize_grade(97) == "A+"


def test_palindrome_checker_1() -> None:
    assert palindrome_checker("hello") == False


def test_palindrome_checker_2() -> None:
    assert palindrome_checker("racecar") == True


# AssertionError
@pytest.mark.xfail
def test_palindrome_checker_3() -> None:
    assert palindrome_checker("yummy") == False
