# Задача1. Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count = 0
# for item in list_1:
#     if item == k:
#         count += 1

# print(count)


# list_1.count(3)

# # Задача 2. Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
import random
n = int(input("Введите число от 1 до 100: "))
temp = [random.randint (1, 101) for i in range(n)]
print(temp)
count = 0
x = int(input("Введите число, к которому ищем ближайшее"))
y = abs(x-temp[0])
z = temp[0]
for i in range(n):
    if abs(x - temp[0])<y:
        y = abs(x-temp[i])
print (z)