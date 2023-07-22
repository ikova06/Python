# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
import random
n = int(input("Введите количество монет: "))
temp = [random.randint (0, 1) for i in range(n)]
print(temp)
a = 0
b = 0

for i in temp:
    if i == 1:
       a= a+1
    if i == 0:
       b = b+1

if a>b:
    print(f"Необходимо перевернуть {b} монеток")
elif a==b:
    print (f"Можно перевернуть любой вид монеток")
else:
    print(f"Необходимо перевернуть {a} монеток")





# print(temp.count(0) if temp.count(0) < temp.count(1) else temp.count(1))

# a = 0
# b = 0
# for i in temp:
#     if i == 1:
#        s += 1
#     else i == 0:
# print(s if s<n/2 else n-s)

# min(s, n-s)


