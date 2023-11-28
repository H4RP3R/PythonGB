# (пользовательский ввод можно заменить на рандомный ввод)
# Пользователь вводит  размер первого массива – N
# и элементы первого массива.
# затем размер второго массива M
# и элементы второго массива
# Нужно вывести те элементы первого массива, которых нет во втором массиве, при этом порядок
# последовательности сохранить исходный

# Ввод: 			Вывод:
# 7			3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1


from random import randint


def get_array(size):
    return [randint(0, 5) for _ in range(size)]


def arr_diff(array1, array2):

    return [num for num in array1 if num not in array2]
    # return [num if num not in array2 else 0 for num in array1]


size_1 = int(input('Введите размер первого массива: '))
size_2 = int(input('Введите размер второго массива: '))

arr_1 = get_array(size_1)
print(f'{arr_1=}')
arr_2 = get_array(size_2)
print(f'{arr_2=}')

res_arr = arr_diff(arr_1, arr_2)
print(*res_arr)
