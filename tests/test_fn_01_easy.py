import pytest

from hacker_functions.fn_01_easy import average, categorize_grade, contains_an_a, is_palindrome, triangle_type


def test_average_1() -> None:
    assert average([5, 6, 7]) == 6.0


def test_average_2() -> None:
    assert average([2, 2, 2]) == 2.0


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_average_3() -> None:
    assert average([])


def test_contains_a_1() -> None:
    assert contains_an_a("hello") == False


def test_contains_a_2() -> None:
    assert contains_an_a("halo") == True


@pytest.mark.xfail(raises=AssertionError)
def test_contains_a_3() -> None:
    assert contains_an_a("b" * 1000 + "a") == True


def test_triangle_type_1() -> None:
    assert triangle_type(3, 3, 3) == "Equilateral"


def test_triangle_type_2() -> None:
    assert triangle_type(3, 3, 4) == "Isosceles"


def test_triangle_type_3() -> None:
    assert triangle_type(3, 4, 5) == "Scalene"


@pytest.mark.xfail(raises=AssertionError)
def test_triangle_type_4() -> None:
    assert triangle_type(3, 4, 3) == "Isosceles"


def test_categorize_grade_1() -> None:
    assert categorize_grade(60) == "D-"


def test_categorize_grade_2() -> None:
    assert categorize_grade(95) == "A"


@pytest.mark.xfail(raises=AssertionError)
def test_categorize_grade_3() -> None:
    assert categorize_grade(97) == "A+"


def test_is_palindrome_1() -> None:
    assert is_palindrome("hello") == False


def test_is_palindrome_2() -> None:
    assert is_palindrome("racecar") == True


@pytest.mark.xfail(raises=AssertionError)
def test_is_palindrome_3() -> None:
    assert is_palindrome("yummy") == False
