"""

    Author: Adam Novak

    Task: Nalezněte nevětší palindromické číslo které je součinem dvou 4 místných čísel.

    Result: 99000099

"""


def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def find_palindrome() -> int:
    for i in range(9999, 999, -1):
        for j in range(9999, 999, -1):
            product = i * j
            if is_palindrome(product):
                return product


print(find_palindrome())
