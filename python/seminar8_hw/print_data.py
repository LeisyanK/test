import edit_bd as ebd
import logger as lg

def print_screen(data):
    for data_key in data:
        print(f'{data_key}: {data[data_key]}')
    # print(*data)
    lg.write_log(f'Вывод на экран: {data}')

def search_worker():
    search_text = input('Введите данные сотрудника: ')
    lg.write_log(f'Поиск сотрудника: {search_text}')
    for elem in ebd.workers:
        # print(elem)
        if search_text in ebd.workers[elem]:
            print(ebd.workers[elem])
            lg.write_log(f'Найдена информация: {ebd.workers[elem]}')

def export_data(db, file=False, typ='a'):  # db - это весь словарь сотрудников, отделов или удаленных сотрудников
    # print(file, db)
    if not file:
        file = input('Введите имя файла: ')
    # if file == 'departments.csv':  # файл отделов перезаписываем, а не добавляем
    #     typ = 'w'
    lg.write_log(f'Экспорт в файл: {file}.')
    with open(file, typ) as f:
        data = ''
        for key in db:
            # if key.isdigit():
            #     data += str(key) + ';'
            # else:
            # print(key)
            # if file != 'deleted_workers.csv':
            data += key + ';'
            for elem in db[key]:
                data += elem + ';'
            data = data[:-1] + '\n'  # убираем последний знак ; и добавляем перенос строки
        f.write(data)
        lg.write_log(f'{data}.')