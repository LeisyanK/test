# 37. Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
#
# *Пример:*
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

list1 = [1, 5, 2, 3, 4, 6, 1, 7]
list2 = []
list2.append(list1[0])
for i, el in enumerate(list1[1:], 1):
    #print(i, el)
    if el > list1[i-1]:
        list2.append(el)
    else:
        if len(list2) > 1:
            print(list2)
        list2 = [el]
if len(list2) > 1:
    print(list2)