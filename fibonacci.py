"""

    Author: Adam Novak

    Task: Uvažujme členy Fibonacciho posloupnosti jejichž hodnota není vyšší než 5.000.000.
          Nalezněte součet sudých členů této části posloupnosti.

    Result: 4613732

"""

prev_num = 0
curr_num = 1
total = 0

while curr_num < 5000000:
    if curr_num % 2 == 0:
        total += curr_num
    aux = curr_num
    curr_num = prev_num + curr_num
    prev_num = aux

print(total)