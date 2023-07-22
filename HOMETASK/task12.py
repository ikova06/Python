# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

from math import *
a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c        
if d < 0:
    print('Эти числа не подходят')
elif d == 0:          
    print(-b / (2*a))
elif d > 0:           
    x1 = (-b - d ** 0.5) / (2*a)
    x2 = (-b + d ** 0.5) / (2*a)
    print(min(x1, x2))
    print(max(x1, x2))