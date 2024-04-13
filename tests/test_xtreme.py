import pytest

from hacker_functions.main import authenticate, convert_to_usd, find_median, is_valid_email, pair_items_in_list, run_command, sum_of_digits


def test_run_command_1() -> None:
    assert run_command("remove", is_admin=True) == "Executed command remove"


def test_run_command_2() -> None:
    assert run_command("remove", is_admin=False) == "Sorry, that's only for admin"


# AssertionError
@pytest.mark.xfail
def test_run_command_3() -> None:
    assert run_command("rEmovE", is_admin=False) == "Sorry, that's only for admin"


def test_is_valid_email_1() -> None:
    assert is_valid_email("tmp@e.com") == True


def test_is_valid_email_2() -> None:
    assert is_valid_email("tmp.com") == False


# AssertionError
@pytest.mark.xfail
def test_is_valid_email_3() -> None:
    assert is_valid_email("tmp.e@com") == True


def test_sum_of_digits_1() -> None:
    assert sum_of_digits(1) == 1


def test_sum_of_digits_2() -> None:
    assert sum_of_digits(123) == 6


# ValueError
@pytest.mark.xfail
def test_sum_of_digits_3() -> None:
    assert sum_of_digits(-123) == 5


def test_convert_to_usd_1() -> None:
    assert convert_to_usd(10, "EUR") == 11.0


def test_convert_to_usd_2() -> None:
    assert convert_to_usd(100, "JPY") == 0.91


# KeyError
@pytest.mark.xfail
def test_convert_to_usd_3() -> None:
    assert convert_to_usd(10, "HSD") == 10


def test_authenticate_1() -> None:
    assert authenticate("guess") == False


def test_authenticate_2() -> None:
    assert authenticate("secret") == True


# IndexError
@pytest.mark.xfail
def test_authenticate_3() -> None:
    assert authenticate("long password")


def test_pair_items_in_list_1() -> None:
    assert pair_items_in_list([1, 2, 5, 9, 0, 0]) == [(1, 2), (5, 9), (0, 0)]


# AssertionError
@pytest.mark.xfail
def test_pair_items_in_list_2() -> None:
    assert pair_items_in_list([1, 2, 3]) == [(1, 2), (3, None)]


def test_find_median_1() -> None:
    assert find_median([1, 2, 4]) == 2


def test_find_median_2() -> None:
    assert find_median([1, 2, 2, 5]) == 2


# AssertionError
@pytest.mark.xfail
def test_find_median_3() -> None:
    assert find_median([1, 2, 4, 5]) == 3
