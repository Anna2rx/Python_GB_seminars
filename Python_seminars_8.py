def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по имени или фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента по имени или фамилии\n"
          "6. Изменить данные абонента по имени или фамилии\n"
          "7. Завершить работу")
    choice = int(input())
    return choice


def print_result(phone_book):
    k=5
    for i in phone_book:
        for key in ['Номер п/п'] + list(i.keys()):
            print(f'|{key.rjust(20)}|', end='')
        print()
        print('----------------------'*k)
        break
    for i, user in enumerate(sorted(phone_book, key=lambda x: x['Фамилия']), 1):
        print_info(user, i)


def print_info(sub, i = 0):
    k = 4
    if i:
        values = [str(i)] + list(sub.values())
        k = 5
    else:
        values = sub.values()
    for value in values:
        print(f'|{value.rjust(20)}|', end='')
    print()
    print('----------------------'*k)


def get_search_surname():
    return input("Введите фамилию для поиска: ").strip()


def find_by_surname(phone_book, surname):
    data = set(find_by(phone_book, 'Фамилия', surname) + find_by(phone_book, 'Имя', surname))
    if data:
        print_result(data)
    else:
        print("Абонент не найден!")


def get_search_number():
    return input("Введите номер телефона для поиска: ").strip()


def find_by(phone_book, param, value):
    data = []
    for i in phone_book:
        if i[param] == value:
            data.append(i)
    return data


def find_by_number(phone_book, number):
    data = find_by(phone_book, 'Телефон', number)
    if data:
        print_result(data)
    else:
        print("Абонент не найден!")


def get_new_user():
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    # return dict(zip(fields, data))
    return {f: input(f"Введите значение для поля '{f}': ") for f in fields}


def add_user(filename, user_data):
    data = read_csv(filename)
    data.append(user_data)
    write_csv(filename, data)
    print("Информация о новом пользователе записана в файл!")


def remove_by_surname(phone_book, surname, filename):
    d = find_by(phone_book, 'Фамилия', surname) + find_by(phone_book, 'Имя', surname)
    data = sorted(d, key=lambda x: x['Фамилия'])
    if data:
        print_result(data)
        number = int(input("Введите порядковый номер абонента, которого хотите удалить: "))
        phone_book.remove(data[number - 1])
        write_csv(filename, phone_book)
        print("Данные успешно удалены!")
    else:
        print("Абонент не найден!")


def change_by_surname(phone_book, surname, filename):
    d = find_by(phone_book, 'Фамилия', surname) + find_by(phone_book, 'Имя', surname)
    data = sorted(d, key=lambda x: x['Фамилия'])
    if data:
        print_result(data)
        number = int(input("Введите порядковый номер абонента, данные о котором хотите изменить: "))
        user = get_new_user()
        i = phone_book.index(d[number - 1])
        phone_book[i] = user
        write_csv(filename, phone_book)
        print("Данные успешно изменены!")
    else:
        print("Абонент не найден!")


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phon.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            surname = get_search_surname()
            find_by_surname(phone_book, surname)
        elif choice == 3:
            number = get_search_number()
            find_by_number(phone_book, number)
        elif choice == 4:
            user_data = get_new_user()
            add_user('phon.txt', user_data)
            phone_book = read_csv('phon.txt')
        elif choice == 5:  # remove
            surname = get_search_surname()
            remove_by_surname(phone_book, surname, 'phon.txt')
            phone_book = read_csv('phon.txt')
        elif choice == 6:  # change
            surname = get_search_surname()
            change_by_surname(phone_book, surname, 'phon.txt')
            phone_book = read_csv('phon.txt')
        elif choice > 7:
            print("Вы ввели слишком большое значение, попробуйте еще раз ")
            print()
        choice = show_menu()


def read_csv(filename):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


work_with_phonebook()
