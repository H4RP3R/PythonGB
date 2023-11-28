# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементами list_1 и границы диапазона в виде чисел min_number, max_number.

# Пример
# На входе:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# На выходе:
# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# Введите ваше решение ниже


def indexes_in_range(arr, min_num, max_num):
    return [idx for idx in range(len(arr)) if min_num <= arr[idx] <= max_num]


indexes = indexes_in_range(arr=list_1, min_num=min_number, max_num=max_number)
for idx in indexes:
    print(idx)
