# Задача №1.  За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной конструкцией if и циклами.
# Input:
# n = 700км/д
# s= 750км
# Output:
# 2


import math

n = int(input('Enter a value for "n": '))
m = int(input('Enter a value for "m": '))
print(math.ceil(m/n))
print(m//n + (m % n > 0))
print((m+n-1)//n)
print(-(-m//n))
