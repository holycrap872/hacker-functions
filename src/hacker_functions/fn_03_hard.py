def run_command(command: str, *, is_admin: bool) -> str:
    """
    Simulate running a command on a computer as either admin or a normal user

    Bug: An oddly cased command that should require admin get's through

    :param command: The command to run
    :param is_admin: Whether the person is an admin user
    :returns: The result of running the command - or a denial if requires admin
    """
    admin_only = ["remove", "download", "create"]
    if not is_admin:
        for c in admin_only:
            if c.lower() == command or c.upper() == command:
                return "Sorry, that's only for admin"

    return f"Executed command {command.lower()}"


def is_valid_email(email: str) -> bool:
    """
    Determines whether a given string is a valid email address

    Bug: Fails to check for the position of . which should be after @

    :param email: Potential email address
    :returns: T/F about whether the `email` was a valid email address
    """
    return "@" in email and "." in email.split("@")[1]


def sum_of_digits(n: int) -> int:
    """
    Adds up all of the digits in a particular number. For example, 12 would
    result in `3` (1 + 2) being returned.

    Bug: Fails to account for negative numbers

    :params n: the number to process
    :returns: The sum of the digits in `n`
    """
    return sum(int(char) for char in str(n))


def convert_to_usd(num_dollars: int, currency: str) -> float:
    """
    Calculate how much money a certain number of dollars would be in another
    denomination

    Bug: Fails to handle cases where currency is not in rates dictionary

    :param num_dollars: The number of dollars to convert
    :param currency: The currency to convert to
    """
    # Converts an amount from a specified currency to USD.
    rates = {"EUR": 1.1, "JPY": 0.0091}
    return num_dollars * rates[currency]


def authenticate(password: str) -> bool:
    """
    Check if a given password matches the secret password. This function mimics
    a "buffer overflow vulnerability", a classic error in languages like C.

    Bug: A too long password "overflows"

    :param password: The password check to see if it matches the secret
    :returns: T/F about whether the password matches
    """
    buffer = [""] * 10
    for i in range(len(password)):
        buffer[i] = password[i]
    return buffer == ["s", "e", "c", "r", "e", "t", "", "", "", ""]


def pair_items_in_list(items: list[int]) -> list[tuple[int, int]]:
    """
    Take a list of integers and create a new list where items 0 and 1 are
    paired, items 2 and 3 are paired, items 4 and 5 are paired ....

    For example [1, 5, 7, 4] -> [(1, 5), (7, 4)].

    Bug: Off-by-one error that manifests only if the list length is odd

    :param items: The list of items to "pair up"
    :returns: The list of paired items
    """
    processed = []

    i = 0
    while i < len(items) - 1:
        # Processes in pairs
        processed.append((items[i], items[i + 1]))
        i += 2

    return processed


def find_median(numbers: list[int]) -> int:
    """
    Find the median (middle) number for a list of numbers

    Bug: Incorrect for even-length lists

    :param numbers: The list of numbers to find the median for
    :returns: The median (middle) number
    """
    sorted_numbers = sorted(numbers)
    return sorted_numbers[len(sorted_numbers) // 2]
