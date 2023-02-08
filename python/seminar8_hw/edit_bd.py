import print_data as pd
import logger as lg

workers = {}
departments = {}
id_worker = 0
deleted_workers = {}
del_work = 0

flag1 = True
with open('departments.csv', 'r') as dep_file:
    while flag1:
        record = dep_file.readline()
        if not record:
            flag1 = False
            print(departments)
            lg.write_log(f'Выгрузка из файла отделов: {departments}')
            print('конец файла отделов')
        else:
            if ';' in record:
                record = record.split(';')
                record[-1] = record[-1].replace('\n', '')
                # print('record=', record)
                # print(departments[record[0]], record[1])
                # print(type(departments[record[0]]), type(record[1]))
                # print(record[0])
                # print(type(record[0]))
                # print(record[1:])
                # print(type(record[1:]))
                departments[record[0]] = record[1:]
                # print(departments[record[0]])
            

flag1 = True
with open('workers.csv', 'r') as work_file:
    while flag1:
        record = work_file.readline()
        if not record:
            flag1 = False
            print(workers)
            lg.write_log(f'Выгрузка из файла сотрудников: {workers}')
            print('конец файла сотрудников')
        else:
            record = record.split(';')
            # if '\n' in record[-1]:
            #     print('есть перенос', record[-1], type(record[-1]))
            record[-1] = record[-1].replace('\n', '')
            # print('worker record=', record)
            # global id_worker
            # print('id_worker=', workers[record[0]])
            id_worker = int(record[0])
            # print(id_worker)
            workers[record[0]] = list(record[1:])   # int ???????????????????????????
            # print(workers)
            # print(workers.keys())
            # print('id_worker=', workers[record[0]])
            # print('данные сотрудника: ', record[1:])
            # id_worker = int(workers[(record[0])])
            # id_worker = int(record[0])
            # print()


flag1 = True
with open('deleted_workers.csv', 'r') as work_file:
    while flag1:
        record = work_file.readline()
        if not record:
            flag1 = False
            print(deleted_workers)
            lg.write_log(f'Выгрузка из файла удаленных сотрудников: {deleted_workers}')
            print('конец файла удаленных сотрудников')
        else:
            record = record.split(';')
            record[-1] = record[-1].replace('\n', '')
            # print('worker record=', record)
            # id_worker = int(record[0])
            del_work = record[0]
            if int(del_work) > int(id_worker):
                id_worker = int(del_work) #+ 1
            # print('id сотрудника ',id_worker)
            # print('id удаленного ', del_work)
            # del_work += 1
            # deleted_workers[str(del_work)] = record[1:]
            # deleted_workers[record[0]] = list(record[1:])
            deleted_workers[record[0]] = record[1:]



def create_department(dep_name=False):
    global departments
    if not dep_name:
        dep_name = input('Введите название нового отдела: ')
    departments[dep_name] = []
    lg.write_log(f'Создали новый отдел: {dep_name}')
    #  записать в БД

def create_worker():
    surname = input('Введите фамилию сотрудника: ')
    name = input('Введите имя сотрудника: ')
    middle_name = input('Введите отчество сотрудника: ')
    birthdate = input('Введите дату рождения сотрудника: ')
    phone = input('Введите номер телефона сотрудника: ')
    address = input('Введите адрес сотрудника: ')
    dep_name = input('Введите отдел сотрудника: ')
    global workers
    if dep_name not in departments:  # workers:
        create_department(dep_name)
    worker = [surname, name, middle_name, birthdate, phone, address, dep_name]
    global id_worker 
    id_worker += 1   
    # workers[id_worker] = worker
    workers[str(id_worker)] = worker
    departments[dep_name].append(str(id_worker))
    # id_worker = str(int(id_worker) + 1)
    # print(id_worker + ': ' + workers[id_worker])
    # print(workers)
    #  записать в БД
    lg.write_log(f'Создали нового сотрудника: {id_worker}, {worker}')

def edit_worker():
    global workers
    pd.print_screen(workers)
    worker_id = input('Введите номер сотрудника: ')
    # new_worker = workers[worker_id]
    surname = input('Введите фамилию сотрудника: ')
    name = input('Введите имя сотрудника: ')
    middle_name = input('Введите отчество сотрудника: ')
    birthdate = input('Введите дату рождения сотрудника: ')
    phone = input('Введите номер телефона сотрудника: ')
    address = input('Введите адрес сотрудника: ')
    dep_name = workers[worker_id][-1]
    # print(dep_name)
    new_worker = [surname, name, middle_name, birthdate, phone, address, dep_name]
    workers[worker_id] = new_worker
    lg.write_log(f'Изменили данные сотрудника: {worker_id}, {new_worker}')

def delete_worker():
    global workers
    pd.print_screen(workers)
    worker_id = input('Введите номер сотрудника: ')
    global deleted_workers
    # global del_work
    # deleted_workers[str(del_work)] = list(worker_id) + workers[worker_id]  # сохранили в БД инфо об удаленном сотруднике
    # del_work += 1
    deleted_workers[worker_id] = workers[worker_id]  # сохранили в БД инфо об удаленном сотруднике
    lg.write_log(f'Удалили сотрудника: {worker_id}, {workers[worker_id]}')
    departments[workers[worker_id][-1]].remove(worker_id)  # удалили запись о сотруднике в данном отделе
    del(workers[worker_id])  # удалили самого сотрудника
    print(deleted_workers)
    

def change_department():
    worker_id = input('Введите номер сотрудника: ')
    new_dep_name = input('Введите новый отдел сотрудника: ')
    global workers
    dep_name = workers[worker_id][-1]  #[6]
    lg.write_log(f'Для сотрудника {worker_id} заменили отдел с {dep_name} на {new_dep_name}')
    global departments
    departments[dep_name].remove(worker_id)  # удалили сотрудника из отдела
    # workers[worker_id].replace(dep_name, new_dep_name)
    workers[worker_id][-1] = new_dep_name  # заменили название отдела (последний элемент списка) на новый
    departments[new_dep_name].append(worker_id)  # добавили сотрудника в новый отдел


# def save_all():
#     pd.export_data(workers, 'workers.csv', 'w')
#     pd.export_data(departments, 'departments.csv', 'w')
#     pd.export_data(deleted_workers, 'deleted_workers.csv', 'w')
    

# create_department('new')
# departments['IT'] = [1,2,3]
# print(departments)

# create_worker()