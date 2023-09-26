"""
    
    Author: Adam Novak
    
    Task: Prvočíselní dělitelé čísla 13195 jsou 5, 7, 13 a 29.
          Nalezněte největší prvočíselný dělitel čísla 70616204741131.
    
    Note: The largest prime factor of a number must be less than or equal to its square root.

    Result: 103608299

"""

number = 70616204741131
factor = 2

while factor**2 <= number:
    if number % factor == 0:
        number //= factor
    else:
        factor += 1

print(number)