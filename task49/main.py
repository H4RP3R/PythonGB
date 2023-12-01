# Задача №49.
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет
# найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды
# таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть
# кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из
# пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей
# эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь.
# Гарантируется, что самая далекая планета ровно одна.

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вывод:
# 2.5 10


from math import pi


def calc_orbit_area(nums):
    return pi * nums[0] * nums[1]


def find_farthest_orbit(orbits):
    planets = [orbit for orbit in orbits if orbit[0] != orbit[1]]
    max_area = max(map(calc_orbit_area, planets))
    farthest_orbit = list(filter(lambda x: calc_orbit_area(x) == max_area, planets))[0]
    return farthest_orbit


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
