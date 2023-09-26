
"""
    
    Author: Adam Novak
    Task: Find LCM in range <1;30>.
    Note: The simplest way to calculate the least common multiple of the numbers 
    n1,...,nx is to decompose these numbers into primes and from the decompositions 
    to select the prime factors in the highest powers. By multiplying them we obtain the LCM.

"""

max_factors = {} 
int_start = 1
int_end = 30

for i in range(int_start, int_end + 1):
    number = i
    factor = 2
    while factor <= number:
        count = 0
        while number % factor == 0:
            count += 1
            number //= factor
        max_factors[factor] = max(max_factors.get(factor, 0), count)
        factor += 1

total = 1
for key, value in max_factors.items():
    total *= key**value

print(total)

