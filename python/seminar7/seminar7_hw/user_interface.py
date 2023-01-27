from logger import log_data as ld

def enter_data():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    description = input('Введите описание номера: ')
    ld(f'Get data from User: {surname}, {name}, {phone} - {description}\n')
    return surname, name, phone, description

# def print_data(surname, name, phone, description):
#     print(surname, name, phone, '-', description)

def print_data(data):
    surname, name, phone, description = data
    # print('Человек:')
    print(surname, name, phone, '-', description)
    ld(f'Print data on the display: {surname}, {name}, {phone} - {description}\n')


# data = enter_data()
# print(data)
# print_data(data)