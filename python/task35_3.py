def polynom_koef(str1):
    i = 0
    while i < len(str1) - 2:
        temp_str = ''
        temp = i
        while str1[i] != '*' and str1[i] != '+' and str1[i] != '-' and str1[i] != '=':
            temp_str += str1[i]
            i += 1
        else:
            if str1[i] == '-':
                temp_str = str1[i] + temp_str
        if 'x' in temp_str:
            if temp_str[:2] == 'x^':
                deg = (temp_str[2:])    # len(temp_str)-1])
                print('deg=', deg)
            else:   # temp_str[0] == 'x':
                deg = '1'   # temp_str[2:]''  # len(temp_str)-1])
                print('_deg=', deg)
        elif str1[i] == '=' and not('x' in temp_str):
            koef = (temp_str)
            print('koef=', koef)
            deg = '0'
            print('deg=', deg)
        else:
            koef = (temp_str)
            print('koef=', koef)
        # print(f'str1{[i]} = {str1[i]}')
        # if str1[i] == '-':
        #     koef = '-' + koef  # число умножаем на -1
        #     print('koef=', koef)
        i += 1


str3 = '-15*x^4-41*x^3+75=0'
d3 = polynom_koef(str3)
print(str3)
# print(d3)