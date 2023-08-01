# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

s = 'a a a b c a a d c d d'.split()
print(s)
my_dict = {}
print(my_dict)
for v in s:
    if v not in my_dict:
        print(v, end=' ') 
        # my_dict[v] = 1
    else:
        print(f'{v}_{my_dict[v]}', end=' ')
        # my_dict[v] += 1
    my_dict[v] = my_dict.get(v, 0) +1 


# stroka = 'a a b c'.split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#         result[i] += 1
#     else:
#         print(i, end=' ')
#         result[i] = 1















#         count = 0
#         if v in my_dict:
#             print(v) 
#         if  my_dict[v] == my_dict[v]:
#             print(f'{v}_{count+1 for my_dict[v] in (s.count(v))}', end=' ')



# my_dict = {n: s.count(n) for n in s}
# for i in s:
#        if i in s:
#         print(f'{i}_{my_dict[i]}',  end=' ')


