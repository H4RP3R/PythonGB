# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


input_data = [1, 5, 3, 3, 5, 3, 4]


def mark_max_to_min(mark_list):
    if len(mark_list) == 1:
        return [(mark_list[0], 1)[mark_list[0] == max(input_data)], ]

    mid = len(mark_list) // 2
    return mark_max_to_min(mark_list[:mid]) + mark_max_to_min(mark_list[mid:])


print(input_data)
print(mark_max_to_min(input_data))
