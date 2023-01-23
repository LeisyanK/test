def main():
    num = int(input('Введите число: '))
    i = 2
    mults = []
    while num >= i * i:  # math.sqrt(num) > i:
        if not num % i:
            mults.append(i)
            num //= i
        else:
            i += 1
    mults.append(num)
    print(mults)

main()