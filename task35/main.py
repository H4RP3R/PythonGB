# Задача №35.
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes


def is_prime_number(number, divisor=2):
    if divisor == number // 2:
        return 'yes'
    elif number % divisor == 0:
        return 'no'

    return is_prime_number(num, divisor+1)


num = int(input('Введите число: '))
print(f'{is_prime_number(num)=}')
