# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
#
# a) Добавьте игру против бота

import random

conf = 20
step = 5
# num = conf + 1
player = random.randint(1, 2)
while conf > 0:
    print('Осталось конфет: ', conf)

    if player == 1:
        player = 2  # бот
        num = random.randint(1, step)
        print(f'Берет компьютер: {num}')
    else:
        player = 1  # человек
        num = int(input('Возьми конфеты: '))
        while num < 1 or num > step or num > conf:
            if num > conf:
                print(f'Осталось только {conf} конфеты!')
            else:
                print(f'Вы можете взять не более {step} конфет! Осталось конфет: {conf}')
            num = int(input('Возьми конфеты: '))
    conf -= num

if player == 1:
    print('Ты победил!')
else:
    print('Победил компьютер!')