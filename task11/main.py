# Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# Input:     21
# Output:  9

# Ряд чисел Фибоначчи:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …


a = input("Input a number: ")

while not a.isdigit() or a == "0" or a == "1":
    print("Error input")
    a = input("Input a number: ")

a = int(a)

pos = 3
pred = 1
pred2 = 1
while pred < a:
    pred, pred2 = pred + pred2, pred
    pos += 1

if pred != a:
    print(-1)
else:
    print(pos)
