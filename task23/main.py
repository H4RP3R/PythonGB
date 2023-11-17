# Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов
# массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения списка или список задан изначально.


data_list = [0, -1, 5, 2, 3]
count = 0

for i in range(len(data_list)-1):
    if data_list[i] < data_list[i+1]:
        count += 1

print(f'{count=}')

new_list = [1 for i in range(len(data_list)-1) if data_list[i] < data_list[i+1]]
print(sum(new_list))

new_list = [1 if data_list[i] < data_list[i+1] else 0 for i in range(len(data_list)-1)]
print(sum(new_list))
