input_data = 'a a a b c a a d c d d'
input_list = input_data.split()


count_dict = {}
for letter in input_list:
    print(f'{letter}{count_dict.get(letter, "")}', end=' ')
    number_letter = count_dict.get(letter, 0) + 1
    count_dict[letter] = number_letter
