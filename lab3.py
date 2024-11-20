print('Введите число 1:')
a = input()
print('Введите число 2:')
b = input()
print('Введите число 3:')
c = input()

if a==b and a==c and b==c:
    print('Все числа 3 равны')

else:
    if a==b and a==c or b==c and b==a:
        print('2 числа равны')

if a!=b and a!=c and b!=c:
    print('Не одно из перечисленных чисел не равно друг другу')