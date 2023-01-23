# import random
#
# k = int(input('Введите значение натуральной степени k: '))
# list_values = [random.randint(0,100) for i in range(k + 1)]
# print(list_values)
#
# list_coefs = [f'{j}*x^{i}' for i, j in enumerate(list_values)]
# list_coefs = list_coefs[::-1]
# list_coefs = ' + '.join(list_coefs)
# print(list_coefs, end='')

import random

k = int(input('Введите значение натуральной степени k: '))
list_values = [random.randint(0,100) for i in range(k + 1)]
print(list_values)

list_coefs = ' + '.join([f'{j}*x^{i}' for i, j in enumerate(list_values)] [::-1])
print(list_coefs, end='')