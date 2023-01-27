import user_interface as ui
import export
import import_file

def button_click():
    print('Здравствуйте! Что Вы хотите сделать?')
    print('Добавить данные - нажмите 1')
    behave1 = input('Получить данные - нажмите 2: ')
    if behave1 == '1':
        # surname, name, phone, description = ui.enter_data()
        data = ui.enter_data()
        # surname, name, phone, description = data
    else:
        data = import_file.import_data()   # здесь весь файл в виде кортежа из строк
        # surname, name, phone, description = data
    print('Хотите сохранить данные в файл?')
    behave2 = input('Введите yes или no: ')
    if behave2 == 'yes':
        file = input('Введите название файла с расширением: ')
        if behave1 == '1':
            if 'txt' in file:
                # export.export_txt(surname, name, phone, description)
                export.export_txt(data)
            elif 'csv' in file:
                export.export_csv(data)
            else:
                print('Некорректный формат файла')
        else:
            # print('controller:: ',data)
            if 'txt' in file:
                for i in range(0,len(data),4):
                    # surname = data[i]
                    # name = data[i+1]
                    # phone = data[i+2]
                    # description = data[i+3]
                    # export.export_txt(surname, name, phone, description)
                    # print(data[i:i+4])
                    export.export_txt(data[i:i+4])
            elif 'csv' in file:
                # export.export_csv(surname, name, phone, description)
                for i in range(0,len(data),4):
                    # surname = data[i]
                    # name = data[i+1]
                    # phone = data[i+2]
                    # description = data[i+3]
                    # export.export_csv(surname, name, phone, description)
                    # print(data[i:i+4])
                    export.export_csv(data[i:i+4])
            else:
                print('Некорректный формат файла')
    elif behave2 == 'no':
        pass
    else:
        print('Некорректный ввод')