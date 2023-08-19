def show_menu():
    print('1. Распечатать справочник\n'
          '2. Найти запись по фамилии, имени или номеру телефона\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Добавить абонента в справочник\n'
          '6. Закончить работу')
    choice=int(input())
    return choice

def read_txt(phonebook):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(phonebook,'r',encoding='utf-8') as phb:
        for line in phb:
            record=dict(zip(fields,line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def read_txt_to_list(phonebook_list):
    with open(phonebook_list, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

def print_contacts(phone_book: list):
    for contact in phone_book:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()
    print('\n')

def find_contact(phone_book):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Телефон'}
    found_contacts = []
    for contact in phone_book:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
            print(search_value)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()

def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value

def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()

def change_phone_number(phonebook_list):
    contact_list = read_txt_to_list('phonebook.txt')
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(phonebook_list, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)

def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    description = input('Введите описание: ')
    return last_name, first_name, phone_number, description

def add_to_phonebook(phonebook):
    info = ','.join(get_new_number())
    with open(phonebook, 'a', encoding='utf-8') as file:
        file.write(f'\n{info}')

def rewrite_all_txt(phonebook,phone_book):
    with open(phonebook,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

def delete_contact(phonebook):
    phone_book = read_txt('phonebook.txt')
    found_contacts = find_contact_to_edit(phone_book)
    phone_book.remove(found_contacts.index)
    with open(phonebook, 'w', encoding='utf-8') as file:
        for contact in phone_book:
            line = ','.join(contact) + '\n'
            file.write(line)


def find_contact_to_edit(phone_book):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Телефон'}
    found_contacts = []
    for contact in phone_book:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
            print(search_value)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        return found_contacts
    print()

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    phonebook_list=read_txt_to_list('phonebook.txt')
    while (choice!=6):
        if choice==1:
            phone_book=0
            phone_book=read_txt('phonebook.txt')
            print_contacts(phone_book)
        elif choice==2:
            find_contact(phone_book)
        elif choice==3:
            change_phone_number(phonebook_list)
        elif choice==4:
            delete_contact('phonebook.txt')
        elif choice==5:
            add_to_phonebook('phonebook.txt')
        choice=show_menu()

work_with_phonebook()