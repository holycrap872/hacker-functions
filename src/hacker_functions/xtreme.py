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
