# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial(n-1)
    
# print(factorial(7))


# Задача No31. Решение в группах
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21

# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
 
# print("Значение этого элемента:", fib2)

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

# def convers(n) :
#     if n == 0 :
#         return "+"
#     ss = input("введите символ:")
#     return convers(n-1)+ss

# def convers2(n) :
#     if n == 0 :
#         return "%"
#     ss = input("введите символ:")
#     return ss+convers2(n-1)
# print(convers(5))
# print(convers2(5))

# Возведение в степень b
# def power(a,b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     else:
#         return a * power(a, b-1)
    
# a = int(input())
# b = int(input())   
# print(power(a,b))

def sum(a,b):
    if b == 0:
        return a
    else:
        return sum(a-1, b+1)
    
a = int(input())
b = int(input()) 

print(sum(a,b))