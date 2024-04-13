from hacker_functions.main import *


def test_average_1() -> None:
    assert average([5, 6, 7]) == 6.0


def test_average_2() -> None:
    assert average([2, 2, 2]) == 2.0


def test_average_3() -> None:
    try:
        assert average([])
    except ZeroDivisionError:
        pass
    else:
        assert False


def test_contains_a_1() -> None:
    assert contains_an_a("hello") == False


def test_contains_a_2() -> None:
    assert contains_an_a("halo") == True


def test_contains_a_3() -> None:
    try:
        assert contains_an_a("b" * 1000 + "a") == True
    except AssertionError:
        pass
    else:
        assert False


def test_triangle_type_1() -> None:
    assert triangle_type(3, 3, 3) == "Equilateral"


def test_triangle_type_2() -> None:
    assert triangle_type(3, 3, 4) == "Isosceles"


def test_triangle_type_3() -> None:
    assert triangle_type(3, 4, 5) == "Scalene"
    try:
        assert triangle_type(3, 4, 3) == "Isosceles"
    except AssertionError:
        pass
    else:
        assert False


def test_find_middle_1() -> None:
    assert find_middle(8, 4, 10) == 8


def test_find_middle_2() -> None:
    assert find_middle(4, 8, 10) == 8


def test_find_middle_3() -> None:
    assert find_middle(10, 4, 8) == 8


def test_find_middle_4() -> None:
    try:
        assert find_middle(10, 4, 10) == 10
    except AssertionError:
        pass
    else:
        assert False


def test_categorize_grade_1() -> None:
    assert categorize_grade(60) == "D-"


def test_categorize_grade_2() -> None:
    assert categorize_grade(95) == "A"


def test_categorize_grade_3() -> None:
    try:
        assert categorize_grade(97) == "A+"
    except AssertionError:
        pass
    else:
        assert False


def test_palindrome_checker_1() -> None:
    assert palindrome_checker("hello") == False


def test_palindrome_checker_2() -> None:
    assert palindrome_checker("racecar") == True


def test_palindrome_checker_3() -> None:
    try:
        assert palindrome_checker("yummy") == False
    except AssertionError:
        pass
    else:
        assert False


def test_count_matches_1() -> None:
    assert count_matches(["hey", "you"], "guys") == 0


def test_count_matches_2() -> None:
    assert count_matches(["hey", "you"], "hey") == 1


def test_count_matches_3() -> None:
    try:
        assert count_matches(["hey", "hey", "hey"], "hey") == 3
    except AssertionError:
        pass
    else:
        assert False


def test_capitalize_first_1() -> None:
    assert capitalize_first("Eric") == "Eric"


def test_capitalize_first_2() -> None:
    assert capitalize_first("eric") == "Eric"


def test_capitalize_first_3() -> None:
    try:
        assert capitalize_first("")
    except IndexError:
        pass
    else:
        assert False


def test_find_in_list_1() -> None:
    assert find_in_list([1, 3, 5, 7], 3) == True


def test_find_in_list_2() -> None:
    assert find_in_list([1, 3, 5, 7], 4) == False


def test_find_in_list_3() -> None:
    try:
        assert find_in_list([7, 5, 3, 1], 3) == True
    except AssertionError:
        pass
    else:
        assert False


def test_strings_equal_1() -> None:
    assert strings_equal("hello", "hello") == True


def test_strings_equal_2() -> None:
    assert strings_equal("shops", "ships") == False


def test_strings_equal_3() -> None:
    try:
        assert strings_equal("hellothere", "hello") == False
    except IndexError:
        pass
    else:
        assert False


def test_max_number_1() -> None:
    assert max_number([1, 3, 5, 7]) == 7


def test_max_number_2() -> None:
    assert max_number([3, 5, 7, 1]) == 7


def test_max_number_3() -> None:
    try:
        assert max_number([]) == True
    except IndexError:
        pass
    else:
        assert False


def test_run_command_1() -> None:
    assert run_command("remove", is_admin=True) == "Executed command remove"


def test_run_command_2() -> None:
    assert run_command("remove", is_admin=False) == "Sorry, that's only for admin"


def test_run_command_3() -> None:
    try:
        assert run_command("rEmovE", is_admin=False) == "Sorry, that's only for admin"
    except AssertionError:
        pass
    else:
        assert False


def test_is_valid_email_1() -> None:
    assert is_valid_email("tmp@e.com") == True


def test_is_valid_email_2() -> None:
    assert is_valid_email("tmp.com") == False


def test_is_valid_email_3() -> None:
    try:
        assert is_valid_email("tmp.e@com") == True
    except AssertionError:
        pass
    else:
        assert False


def test_sum_of_digits_1() -> None:
    assert sum_of_digits(1) == 1


def test_sum_of_digits_2() -> None:
    assert sum_of_digits(123) == 6


def test_sum_of_digits_3() -> None:
    try:
        assert sum_of_digits(-123) == 5
    except ValueError:
        pass
    else:
        assert False


def test_convert_to_usd_1() -> None:
    assert convert_to_usd(10, "EUR") == 11.0


def test_convert_to_usd_2() -> None:
    assert convert_to_usd(100, "JPY") == 0.91


def test_convert_to_usd_3() -> None:
    try:
        assert convert_to_usd(10, "HSD") == 10
    except KeyError:
        pass
    else:
        assert False


def test_authenticate_1() -> None:
    assert authenticate("guess") == False


def test_authenticate_2() -> None:
    assert authenticate("secret") == True


def test_authenticate_3() -> None:
    try:
        assert authenticate("long password")
    except IndexError:
        pass
    else:
        assert False


def test_pair_items_in_list_1() -> None:
    assert pair_items_in_list([1, 2, 5, 9, 0, 0]) == [(1, 2), (5, 9), (0, 0)]


def test_pair_items_in_list_2() -> None:
    try:
        assert pair_items_in_list([1, 2, 3]) == [(1, 2), (3, None)]
    except AssertionError:
        pass
    else:
        assert False


def test_find_median_1() -> None:
    assert find_median([1, 2, 4]) == 2


def test_find_median_2() -> None:
    assert find_median([1, 2, 2, 5]) == 2


def test_find_median_3() -> None:
    try:
        assert find_median([1, 2, 4, 5]) == 3
    except AssertionError:
        pass
    else:
        assert False
