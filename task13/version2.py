days_num = int(input("Введите кол-во дней: "))

max_thaw_days = 0
thaw_days = 0
for i in range(days_num):
    temperature = int(input("Введите температуру: "))
    if temperature > 0:
        thaw_days += 1
        if thaw_days > max_thaw_days:
            max_thaw_days = thaw_days
    else:
        thaw_days = 0

print()
print(f'{max_thaw_days=}')
