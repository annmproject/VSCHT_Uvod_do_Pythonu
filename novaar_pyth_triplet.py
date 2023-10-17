"""

    Author: Adam Novak

    Task: Nalezňete Pythagorejsou trojici pro kterou platí, že  a + b + c = 1000.
          Jaky je součin této trojice?

    Result: 31875000

"""


def triplet(total: int) -> int:
    for a in range(1, total):
        for b in range(1, total):
            c = total - a - b
            if c > 0:
                if a + b + c == total:
                    if a**2 + b**2 == c**2:
                        return a * b * c
    return -1


print(triplet(1000))
