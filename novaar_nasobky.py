
"""

    Author: Adam Novak

    Task: Uvažujme přirozená čísla menší než 10, který jsou násobky 3 nebo 5 (tj. 3; 5; 6; 9).
          Součet těchto násobků je 23. Určete součet všech násobků 3 a 5 menších než 1234.

    Result: 354858

"""

total = 0

for num in range(1234):
    if num % 3 == 0 or num % 5 == 0:
        total += num

print(total)