# Задача 13. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это
# самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует,
# сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

#  Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50.
#  Нужно вывести наибольшее количество идущих подряд положительных чисел.

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random


days_num = int(input("Введите кол-во дней: "))

max_thaw_days = 0
thaw_days = 0
for i in range(days_num):
    temperature = random.randint(-50, 50)
    print(temperature, end=" ")
    if temperature > 0:
        thaw_days += 1
    else:
        if thaw_days > max_thaw_days:
            max_thaw_days = thaw_days
        thaw_days = 0

if thaw_days > max_thaw_days:
    max_thaw_days = thaw_days

print()
print(f'{max_thaw_days=}')
