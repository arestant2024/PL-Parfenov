def NOD1(a, b):
    if b == 0:
        return a

    else:
        return NOD1(b, a % b)

a = int(input('Первое число: '))
b = int(input('Второе число: '))
NOD2 = NOD1(a, b)
print(f"НОД чисел {a} и {b}: {NOD2}")
print(f"НОК чисел {a} и {b}: ", (a*b)/NOD2)