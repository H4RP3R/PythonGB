# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no


a = 2
b = 6
c = 10

# Введите ваше решение ниже
if (a*b > c) and (c % a == 0 or c % b == 0):
    print('yes')
else:
    print('no')
