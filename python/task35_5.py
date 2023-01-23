def polynom_koef(str1):
    i = 0
    d = {}
    deg = 0
    koef = 0
    max_pow = int(str1[str1.find('^')+1])
    while i < len(str1) - 2:
        temp_str = ''
        temp = i
        while str1[i] != '*' and str1[i] != '+' and str1[i] != '-' and str1[i] != '=':
            temp_str += str1[i]
            i += 1
        if 'x' in temp_str:
            if 'x^' in temp_str:   # temp_str[:2] == 'x^':
                deg = int(temp_str[2:])    # len(temp_str)-1])
            else:   # temp_str[0] == 'x':
                deg = 1   # temp_str[2:]''  # len(temp_str)-1])
            d[deg] = koef
        elif str1[i] == '=' and not('x' in temp_str):
            koef = int(temp_str)
            deg = 0
            d[deg] = koef
        else:
            if str1[temp-1] == '-':
                koef = int('-' + temp_str)  # число умножаем на -1
            elif temp_str != '':
                koef = int(temp_str)
        i += 1
    for j in range(max_pow, -1, -1):
        if not(j in d.keys()):
            # print(j)
            d[j] = 0
    return d, max_pow


str3 = '-15*x^4-41*x^3+75*x-8=0'
d3, pow3 = polynom_koef(str3)
print(str3)
print(d3)
print(pow3)