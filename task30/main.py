# Заполните массив элементами арифметической прогрессии. Её первый элемент a1,
# разность d и количество элементов n будет задано автоматически. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример
# На входе:
# a1 = 2
# d = 3
# n = 4

# На выходе:
# 2
# 5
# 8
# 11

a1 = 7
d = 2
n = 5

# Введите ваше решение ниже


def f(a1, d, n):
    if n == 0:
        return
    f(a1, d, n-1)
    print(a1 + (n-1) * d)


f(a1, d, n)