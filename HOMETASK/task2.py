# Задача 2: Найдите сумму цифр трехзначного числа. 

n = int (input('Введите целое трехначное число: '))
n = int (n)
sum = (n//100) + ((n//10)%10) + (n%10)
print ("Сумма цифр числа = " ,sum)
