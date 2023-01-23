def polynom_koef(str1):
    i = 0
    d = {}
    deg = 0
    koef = 0
    while i < len(str1) - 2:
        temp_str = ''
        temp = i
        # print(f'str[{i}] =', str1[i])
        while str1[i] != '*' and str1[i] != '+' and str1[i] != '-' and str1[i] != '=':
            temp_str += str1[i]
            # print(f'str[{i}] =', str1[i])
            i += 1
        # else:
        #     if str1[i] == '-':
        #         temp_str = str1[i] + temp_str
        if 'x' in temp_str:
            if 'x^' in temp_str:   # temp_str[:2] == 'x^':
                deg = int(temp_str[2:])    # len(temp_str)-1])
                print('deg=', deg)
            else:   # temp_str[0] == 'x':
                deg = 1   # temp_str[2:]''  # len(temp_str)-1])
                print('_deg=', deg)
            d[deg] = koef
        elif str1[i] == '=' and not('x' in temp_str):
            koef = int(temp_str)
            print('for deg=0 koef=', koef)
            deg = 0
            print('deg=', deg)
            d[deg] = koef
        else:
            print(f'str[{temp - 1}]', str1[temp - 1])
            if str1[temp-1] == '-':
                koef = int('-' + temp_str)  # число умножаем на -1
                print('with - koef=', koef)
            elif temp_str != '':
                    # print(temp_str)
                koef = int(temp_str)
                print('all koef=', koef)
        # print(f'str1{[i]} = {str1[i]}')
        # if str1[i] == '-':
        #     koef = '-' + koef  # число умножаем на -1
        #     print('koef=', koef)
        # print(deg, koef)
        # d[deg] = koef
        i += 1
    return d


str3 = '-15*x^4-41*x^3+75*x-8=0'
d3 = polynom_koef(str3)
print(str3)
print(d3)