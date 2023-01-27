from user_interface import enter_data as ed
from logger import log_data as ld

def export_txt(data):   # на вход приходит кортеж из пяти или кратных пяти строковых элементов
    # surname, name, phone, description = ed()
    # file = input('Введите название файла без расширения: ')
    # print(len(data))   # количество элементов кортежа с данными
    file = 'phones.txt'
    with open(file, 'a') as person:
        if len(data) < 6:
            surname, name, phone, description = data
            person.write(surname + '\n')
            person.write(name + '\n')
            person.write(phone + '\n')
            person.write(description + '\n')
            person.write('\n')
            ld(f'Write data into the text file: {surname}, {name}, {phone} - {description}\n')
        else:
            for i in range(0,len(data),5):
                surname = data[i]
                name = data[i+1]
                phone = data[i+2]
                description = data[i+3]
                sep = data[i+5]
                person.write(surname + '\n')
                person.write(name + '\n')
                person.write(phone + '\n')
                person.write(description + '\n')
                person.write(sep + '\n')
                ld(f'Write data into the text file: {surname}, {name}, {phone} - {description}\n')

# def export_csv(surname, name, phone, description):
def export_csv(data):
    # surname, name, phone, description = ed()
    # file = input('Введите название файла без расширения: ')
    file = 'phones.csv'
    with open(file, 'a') as person:
        if len(data) < 6:
            surname, name, phone, description = data
            person.write(surname + ';')
            person.write(name + ';')
            person.write(phone + ';')
            person.write(description + '\n')
            # data.write('\n')
            ld(f'Write data into the table: {surname}, {name}, {phone} - {description}\n')
        else:
            for i in range(0,len(data),5):
                surname = data[i]
                name = data[i+1]
                phone = data[i+2]
                description = data[i+3]
                sep = data[i+5]
                surname, name, phone, description = data
            person.write(surname + ';')
            person.write(name + ';')
            person.write(phone + ';')
            person.write(description + '\n')
            # data.write('\n')
            ld(f'Write data into the table: {surname}, {name}, {phone} - {description}\n')

# export_csv()