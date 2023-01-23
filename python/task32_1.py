import random

def get_arr(num):
    my_L = []
    for i in range(num):
        my_L.append(random.randint(1,10))
    return my_L

def del_el (in_L):
    temp = []
    i = 0
    while i < len(in_L)-1:
        if in_L[i] in in_L[i+1:]:
            temp.append(in_L[i])
        i=i+1
    return (list(set(in_L) - set(temp)))

def main():
    number = int(input('введите размер списка '))
    arr = get_arr(number)
    print(arr)
    print(del_el(arr))


if __name__ == "__main__":
    main()