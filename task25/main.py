# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
# каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


input_data = 'a a a b c a a d c d d'
input_list = input_data.split()

output = ''
count_dict = {}
for letter in input_list:
    output += letter
    if letter in count_dict:
        count_dict[letter] += 1
        output += f'_{count_dict[letter]}'
    else:
        count_dict[letter] = 0
    output += ' '

print(output)
