# Задача1. Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

# list_1 = [1, 2, 3, 4, 5]
# # k = 3
# count = 0
# for item in list_1:
#     if item == k:
#         count += 1

# print(count)


N = int(input('Кол. чисел:'))
a=[int(input('Ввести число:')) for i in range(N)]
x=int(input('Заданное число:'))
b=[abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])
