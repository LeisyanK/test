def polynom_koef(str1):
    d = {}
    temp = 0
    i = 0
    degree = int(str1[str1.find('^') + 1])  # max степень х   # print(degree)
    print('max степень =', degree)
    while i < len(str1) - 1:
        print(str1[i], end=' ')
        if str1[i] == '*':
            koef = int(str1[temp:i])
            if str1[i + 1] == 'x' and str1[i + 2] != '^':
                deg = 'x^1'
                current_deg = 1
                i += 2
                # temp = i
            else:
                deg = str1[i + 1:i + 4]
                current_deg = int(str1[i + 3])
                i += 4
                # temp = i
            d[deg] = koef
            print('degree=', degree, 'cur_deg=', current_deg)
            degree -= 1
            # i += 4
            temp = i
        elif str1[i] == '=' and temp != i:
            # if degree != 0:
            # for j in range(degree, 0, -1):
            #     deg = 'x^' + str(j)
            #     d[deg] = 0
            # if not(str1[i-1] != 'x' or str1[i-3:i-1] != 'x^'):
            deg = 'x^0'
            koef = int(str1[temp:i])
            d[deg] = koef
            break
            # i += 1
        else:
            i += 1
    # нужно пробежаться по словарю и добавить недостоющие коээфициенты???
    return d


str3 = '15*x^4-41*x^3+75=0'
d3 = polynom_koef(str3)
print(str3)
print(d3)