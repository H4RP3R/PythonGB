from random import randint

size_arr_new = int(input('Введите размер массива: '))

arr_new = [randint(0, 5) for _ in range(size_arr_new)]

print(arr_new)

count = 0

for i in range(1, len(arr_new)-1):
    if arr_new[i-1] < arr_new[i] > arr_new[i+1]:
        count += 1
print(count)
# var2
print(sum([1 for i in range(1, len(arr_new)-1) if arr_new[i-1] < arr_new[i] > arr_new[i+1]]))
