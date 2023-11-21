input_data = 'a a a b c a a d c d d'.split()
result = {}
for letter in input_data:
    if letter in result:
        print(f'{letter}_{result[letter]}', end=' ')
    else:
        print(letter, end=' ')
    result[letter] = result.get(letter, 0) + 1
