from math import sqrt
a = int(input('Введите А:'))
b = int(input('Введите B:'))
c = int(input('Введите C:'))

disc = b ** 2 - 4 * a * c
if disc < 0:
    print('Корней нет')
elif not disc:
    print('Корень = ', -b / (2 * a))
else:
    print('Первый корень = ', round((-b - sqrt(disc)) / (2 * a), 2))
    print('Второй корень = ', round((-b + sqrt(disc)) / (2 * a), 2))