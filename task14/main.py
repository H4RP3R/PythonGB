# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
# n=16
# #Вывод
# 1
# 2
# 4
# 8
# 16


# Введите ваше решение ниже
n, k, res = 10, 1, 1
while res <= n:
    print(res)
    res = 2**k
    k += 1
