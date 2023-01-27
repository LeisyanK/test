# file('file2.txt','w').write( file('file.txt').read().encode('utf-8') )
import user_interface as ui
from logger import log_data as ld

def import_data():
    # file = input('Введите название файла без расширения: ')
    file = 'phones.txt'
    with open(file, 'r') as person:
        # ЗДЕСЬ ПОСТРОЧНОЕ ИЗВЛЕЧЕНИЕ ИНФОРМАЦИИ!
        flag = True
        return_data = ()   #''
        while flag:
            surname = person.readline()
            if not surname:     
                flag = False
            else:
                name = person.readline()
                phone = person.readline()
                description = person.readline()
                sep = person.readline()  # разделитель между записями
                # return_data += surname + name + phone + description
                data = (surname[:len(surname)-1], name[:len(name)-1], phone[:len(phone)-1], description[:len(description)-1])
                return_data += data

                ld(f'Get data from DataBase: {data}\n')   #{surname}, {name}, {phone} - {description}')  

                ui.print_data(data)
        return return_data      


# import_data()