"""
    
    Author: Adam Novak
    Task: Find the largest prime factor of the number 70616204741131.
    Note: The largest prime factor of a number must be less than or equal to its square root.

"""

number = 70616204741131
factor = 2

while factor**2 <= number:
    if number % factor == 0:
        number //= factor
    else:
        factor += 1

print(number)