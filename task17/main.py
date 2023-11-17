# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Примечание: Пользователь может вводить значения списка или список задан изначально.


from random import randint


list_length = randint(5, 10)
print(f'{list_length=}')

# num_list = []
# for _ in range(list_length):
#     new_num = randint(0, 5)
#     num_list.append(new_num)

num_list_2 = [randint(0, 5) for _ in range(list_length)]

print(num_list_2)
unique = set(num_list_2)
print(unique)
print(f'{len(unique)=}')
