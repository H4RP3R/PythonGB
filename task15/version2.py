from random import randint


num = randint(1, 20)
weight = randint(5, 15)
print(weight, end=' ')
min_weight = weight
max_weight = weight

for _ in range(num - 1):
    weight = randint(5, 15)
    print(weight, end=' ')
    max_weight = max(max_weight, weight)
    min_weight = min(min_weight, weight)

print()
print(min_weight, max_weight)
