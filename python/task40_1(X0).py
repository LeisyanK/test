import random


def field(my_list):
    print('   | X1| X2| X3|')
    print('----------------')
    for i in 0, 1, 2:
        print(f'Y{i + 1} |', end='')
        for j in 0, 1, 2:
            print(f' {my_list[i][j]} |', end='')  # {my_list[0][1]} | {my_list[0][2]} |')
        print()
        print('----------------')
    # print(f'Y2 | {my_list[1][0]} | {my_list[1][1]} | {my_list[1][2]} |')
    # print('----------------')
    # print(f'Y3 | {my_list[2][0]} | {my_list[2][1]} | {my_list[2][2]} |')
    # print('----------------')


# play = [[' 1',' 2',' 3'],[' 4',' 5',' 6'],[' 7',' 8',' 9']]
play = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
field(play)
player = random.randint(1, 2)
# if player == 1:
#     print('Ты начинаешь игру')
#     x = int(input('Введите х: '))
#     y = int(input('Введите y: '))
# else:
#     print('Компьютер начинает игру')
#     x = random.randint(1, 3)
#     y = random.randint(1, 3)

    # if player == 1:     # man
    #     print('Твой ход: ')
    #     x = int(input('Введите х: '))
    #     y = int(input('Введите y: '))
    # else:               # comp
    #     print('Компьютер ходит: ')
    #     x = random.randint(0, 2)
    #     y = random.randint(0, 2)
flag = True
x = 1
y = 1
while flag:  # flag = True - никто не выиграл
    # while play[x][y] != ' ' and (x not in [0, 1, 2] or y not in [0, 1, 2]):
    while play[x][y] != ' ':
        # ввод х у
        if player == 2:
            print('Компьютер начинает игру')
            x = random.randint(1, 3)
            y = random.randint(1, 3)
        else:
            print('Ты начинаешь игру')
            x = int(input('Введите х: '))
            y = int(input('Введите y: '))

            while (x not in [1, 2, 3] or y not in [1, 2, 3]):
        # if player == 2:
        #     x = random.randint(1, 3)
        #     y = random.randint(1, 3)
        # else:
        #     # if play[x][y] != ' ':
        #     #     print('Клетка уже занята')
        #     # else:
                print('Введите верные значения Х и Y!')
                x = int(input('Введите х: '))
                y = int(input('Введите y: '))
    if x == 3 and y == 3:
        flag = False

# x = int(input('Введите х: '))
# y = int(input('Введите y: '))
# # print(play[1][1])
# if play[x][y]:  # если поле пустое
#     print('Поле уже занято')
# else:
#     play[x][y] = 'x'
#     print(play[x][y])
# print(play)

# field(play)