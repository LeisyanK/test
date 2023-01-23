my_list = ['abc', '45', 'def', 'kmds', 'def', '875']
find = 'def'
num = 2
count = 0
for i in range(len(my_list)):
    if my_list[i] == find:
        count += 1
        if count == num:
            print(i)
            break
# if count == 0: # not count:
else:
    print('В списке нет такой строки')