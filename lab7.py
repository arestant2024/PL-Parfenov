p, s = 1, 0
A = [int(i) for i in input().split()]
for a in A:
    s += a; p *= a
print('Сумма списка:', s)
print('Произведение:', p)

import random as rand

n = int(input("n= "))

if n>0:
    lst=[-3+6*rand.random() for i in range(n)]
    print(lst)
    sr=sum(lst)/len(lst)
    for k,x in enumerate(lst):
        if x==0:
            lst[k]=sr
    print(lst)
