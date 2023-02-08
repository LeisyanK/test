from datetime import datetime

def write_log(data):
    time = datetime.now()
    file = 'log.txt'
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{time}: {data}\n')

def print_log():
    print('Вывод не реализован! Посмотрите в файле log.txt.')
    # with open('log.txt', 'r', encoding="utf-8") as f:
    #     print('Вывод лога:')
    #     write_log(f'Вывод лога на экран:')
    #     data = f.read()
    #     print(data)
    #     write_log(f'{data}')
    #     print('Конец лога.')
    #     write_log('Вывод лога на экран завершен.')

def delete_log():
    time = datetime.now()
    with open('log.txt', 'w', encoding='utf-8') as f:
        f.write(f'{time}: Запрос на удаление лога.\n')
    # write_log(f'{time}: Запрос на удаление лога.')