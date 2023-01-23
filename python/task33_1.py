from random import randint
def polynomial_creation(degree): # Функция создания многочлена
    polynomial = [str(randint(0, 10)) + '*x^' + str(de) for de in range(degree, -1, -1)]
    print(polynomial)
    polynomial = [el for el in polynomial if el[0] != '0']
    print(polynomial)
    polynomial = ' + '.join(polynomial)
    print(polynomial)
    polynomial = polynomial.replace('*x^0', '').replace('x^1 ', 'x ') + ' = 0'  # неправильно записываются степени
    return polynomial


def main():
    number = int(input('введите степень '))
    print(polynomial_creation(number))


main()