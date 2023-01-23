num_str = '87 94 54 76 23 73 23 65'
# num_str = input('Введите набор чисел через пробел:')
num_list = list(map(int,num_str.split()))
print(num_list)
max_num = num_list[0]
min_num = num_list[0]
for el in num_list:
    if el < min_num:
        min_num = el
    elif el > max_num:
        max_num = el
print(min_num, max_num)