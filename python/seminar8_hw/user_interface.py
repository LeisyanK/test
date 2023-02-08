import edit_bd as ebd
import print_data as pd
import logger as lg

def user_choice():
    # lg.write_log('Запуск программы')
    while True:
        print('''Выберите действие:
                1. Добавить отдел
                2. Добавить сотрудника
                3. Редактировать личные данные сотрудника
                4. Перевести сотрудника в другой отдел
                5. Удалить сотрудника
                6. Вывести информацию о сотрудниках на экран
                7. Вывести информацию об отделах на экран
                8. Поиск сотрудника и вывод его данных на экран
                9. Экспорт информации о сотрудниках в файл (тип файла (расширение) вводит пользователь)
                10. Вывод лога на экран
                11. Очистка лога
                12. Выход''')
        choice = input('Введите цифру действия: ')
        lg.write_log(f'Пользователь выбрал {choice} пункт.')
        if choice == '1':
            ebd.create_department()
        elif choice == '2':
            ebd.create_worker()
        elif choice == '3':
            ebd.edit_worker()
        elif choice == '4':
            ebd.change_department()
        elif choice == '5':
            ebd.delete_worker()
        elif choice == '6':
            pd.print_screen(ebd.workers)
        elif choice == '7':
            pd.print_screen(ebd.departments)
        elif choice == '8':
            pd.search_worker()
        elif choice == '9':
            pd.export_data(ebd.workers, '', 'a')
        elif choice == '10':
            lg.print_log()
        elif choice == '11':
            lg.delete_log()
        elif choice == '12':
            #  записать в БД !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # ebd.save_all()
            pd.export_data(ebd.workers, 'workers.csv', 'w')
            pd.export_data(ebd.departments, 'departments.csv', 'w')
            pd.export_data(ebd.deleted_workers, 'deleted_workers.csv', 'w')
            print('Завершение работы')
            break
        else:
            print('Вы ввели некорректное число: ')
            lg.write_log(f'Некорректный ввод: {choice}.')
            user_choice()