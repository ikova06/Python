# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

s = 'a a a b c a a d c d d'.split()
my_dict = {n: s.count(n) for n in s}
for i in s:
       if i in s:
        print(f'{i}_{my_dict[i]}',  end=' ')





#  my_dict[i] = my_dict.get(i,0) + 1




# {n: s.count(n) for n in s}
# for i in s:
#     if i in s:
#         print(f'{i}_{my_dict[i]}')
#     else:
#         print(i, " ")
#         my_dict[i] = my_dict.get(i,0) + 1

    
    # if item in s1:
#     	print(f'{i}_{s1[i]}', end=' ')
# else:
#         print(item, end=' ')
# s1[i] = s1.get(i, 0) + 1

# print(my_dict)












# s1 = input("a a a b c a a d c d d").split()
# def count_duplicates(lst):
#     counts = {}  # Создаем пустой словарь для подсчета повторений
#     for item in lst:
#         if item in counts:
#             counts[item] += 1  # Увеличиваем значение для существующего элемента
#         else:
#             counts[item] = 1  # Добавляем новый элемент в словарь с начальным значением 1

#     return counts

# my_list = s1
# duplicates = count_duplicates(my_list)
# for item, count in duplicates.items():
#     if item in s1:
#     	print(f'{i}_{s1[i]}', end=' ')
# else:
#         print(item, end=' ')
# s1[i] = s1.get(i, 0) + 1
