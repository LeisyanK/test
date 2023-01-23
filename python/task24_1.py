# через int-овый тип неправильно получается
import random

def new_list(n):
    list1 = []
    for _ in range(n):
        list1.append(str(round(random.uniform(0.0, 100.99), 2)))
    return list1

def fraction_diff(list1):
    poz = list1[0].find('.')
    # print('poz = ', poz, end = ' ')
    frac = int(list1[0][poz+1:])
    # print('frac = ', frac)
    # print(type(list1[0][poz+1:]))
    min_f = frac #int(list1[0][poz+1:])
    max_f = frac #int(list1[0][poz+1:])
    for i in range(1, num):
        poz = list1[i].find('.')
        # print('poz = ', poz, end = ' ')
        if poz:
            frac = int(list1[i][poz+1:])
            # print('frac = ', frac)
            if not min_f:
                min_f = frac
                # print('min = ', frac)
            if frac < min_f and frac > 0:
                min_f = frac
                # print('min = ', frac)
            elif frac > max_f:
                max_f = frac
    # print('= ', max_f - min_f)
    print('max = ', max_f, 'min =', min_f)
    return max_f - min_f

num = int(input('Введите количество элементов списка: '))
my_list = new_list(num)
print(my_list)
# если первый элемент с нулевой дробной частью
# my_list[0] = '0.00'
# print(my_list)
print('Разность между максимальной и минимальной дробными частями = ', fraction_diff(my_list))