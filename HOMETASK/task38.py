def read_txt (phonebook):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(phonebook,'r',encoding='utf-8') as phb:
        for line in phb:
            # record=dict(zip(fields,line.strip().split(',')))
            record=dict(zip(fields.line.strip().split(',')))
            phone_book.append(record)
        return phone_book

def print_result (phonebook):
    print(*phonebook, sep='\n')
    print('\n')

def find_by_lastname (phonebook, last_name):
    d =dict
#     last_name = list(filter(lambda x: 'Иванов' in x, phonebook)) 
#     print(last_name)

# def get_name():
#     name = input('Имя:')
#     return name

# def get_number():
#     number = input('№ телефона:')
#     return number

# def data_coliection():
#     return (get_surname(), get_number())


# def find_by_lastname (phonebook, last_name):
#     # res = input()
#     # d=dict(contacts)
#     last_name_and_key = ("'Фамилия': '" + last_name + "'")
#     value=last_name
#     if value in phonebook:
#         print(*phonebook, sep='\n')
#         print(value)
#         print("Found")
#         # print(res + " is " + str(d[res]))
#     else:
#         print(*phonebook, sep='\n')
#         print(value)
#         print("Not found")
    # if lastname in phonebook:
    #     print(lastname + " is " + str(phonebook[res]))
    # else:
    #     print("Not found")
    # if "Иванов" in phonebook:
    #     print("Есть в справочнике")
    # else:
    #     print("Такого человека нет")


    
def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        choice=show_menu()



def show_menu():
    print('1. Распечатать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Закончить работу')
    choice=int(input())
    return choice




# def write_txt(phonebook,phone_book):
#     with open('phonebook.txt','w',encoding='utf-8') as phout:
#         for i in range(len(phone_book)):
#             s=''
#             for v in phone_book[i].values():
#                 s+=v+','
#             phout.write(f'{s[:-1]}\n')

work_with_phonebook()