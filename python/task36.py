# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

file1 = open('file36.txt','r')
nums = file1.read().split()
file1.close()

nums = list(map(int, nums))
print(nums)
for i, el in enumerate(nums[1:], 1): #range(len(nums)):
    # print(i, end=' - ')
    # print(el)
    if nums[i - 1] + 1 != el:
        print(nums[i - 1] + 1)

print('Second variant')
n = [1, 2, 3, 4, 5, 6, 8, 9, 11, 12]
print(n)
print(*[n[i] + 1 for i, val in enumerate(n[1:]) if val != n[i] + 1])

print('Third variant')
my_list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = list()
new_list.append(my_list[0])
print(len(new_list))
#counter = 0
for index in range(len(my_list)):
    if my_list[index] > new_list[-1]:
        new_list.append(my_list[index])
        #counter += 1
print(new_list)