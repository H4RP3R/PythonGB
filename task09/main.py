# Задача №9.  По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input:       5
# Output:    120

x = input("Input a number:  ")

while not x.isdigit() or x == '0':
    print("Error input: ")
    x = input("Input a number:  ")

# x = int(x)
# fact = 1
# num = 1
# while num <= x:
#   fact, num = fact*num, num + 1
# print(fact)

# variant 2

x = int(x)
fact = 1

while x > 1:
    fact, x = fact*x, x - 1

print(fact)
