def polynom_koef(str1):
    d = {}
    temp = 0
    i = 0
    degree = int(str1[str1.find('^')+1])      # max степень х   # print(degree)
    print('max степень =', degree)
    while i < len(str1)-1:
        if str1[i] == '*':
            koef = int(str1[temp:i])
            if str1[i+1:i+3] == 'x^': # and str1[i+2] == '^':
                current_deg = int(str1[i+3])
                print('current_deg', current_deg)
                if degree != current_deg:
                    print('пропущена степень', degree)
                    for j in range(current_deg, degree+1):
                        deg = 'x^' + str(j)
                        d[deg] = 0
                    degree = current_deg
                d[str1[i + 1:i + 4]] = koef  # print(d)
                i += 4
                degree -= 1  # int(str1[i+3])             # степень х
                print(i, 'следующая степень:', degree)
            elif str1[i+1] == 'x' and str1[i+2] != '^':  # x^1
                if degree != current_deg:
                    print('пропущена степень', degree)
                    for j in range(current_deg, degree + 1):
                        deg = 'x^' + str(j)
                        d[deg] = 0
                    degree = current_deg
                # degree -= 1
                d['x^1'] = koef
                i += 2                              # print('flag1', end=' ')
        elif str1[i] == '+' or str1[i] == '-':
            temp = i                                # print('temp = ', end=' ')
            i += 1
        elif str1[i] == '=':  # x^0
            if str1[i - 1] != 'x':
                # if degree == 2:  # не было степени ^1
                #     d['x^1'] = 0
                koef = int(str1[temp:i])
                d['x^0'] = koef  # print('flag2', end=' ')
            else:
                d['x^0'] = 0
            i += 1
        else:
            i += 1

        # else:
        #     i += 1
        # if str1[i] == '=':     # x^0
        #     if str1[i-1] != 'x':
        #         if degree == 2:  # не было степени ^1
        #             d['x^1'] = 0
        #         koef = int(str1[temp:i])
        #         d['x^0'] = koef                         # print('flag2', end=' ')
        #     else:
        #         d['x^0'] = 0
    return d


str1 = '96*x^7+8*x^6+67*x^5+97*x^4+89*x^3+81*x^2+91*x+54=0'
str2 = '15*x^4+41*x^3+60*x^2+75*x+59=0'
str3 = '15*x^4+41*x+75=0'
d3 = polynom_koef(str3)
print(str3)
print(d3)
# print(d1.keys())
# d3 = {}
