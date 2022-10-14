def isint(x):
    try:
        int(x)
        return 1
    except ValueError:
       return 0

    
def isfloat(x):
    try:
        float(x)
        return 1
    except ValueError:
        return 0
    
def poiskmax(a):
    m=a[0]
    for i in range(len(a)):
        if a[i]>m:
            m=a[i]
            global k
            k=i
    print('Максимальный элемент:',m)

def zero(x,k):
    for i in range(k+1,len(x)):
        x[i]=0
    print("Полученный массив:", *x)

a=[]
N=input("Введите количество элементов в массиве: ")
if isint(N)==0:
    while isint(N)!=1:
        print('Ошибка! Введите число!')
        N=input("Введите количество элементов в массиве: ")
N=int(N)
x=input("Введите элемент массива: ")
if isfloat(x)==0:
    while isfloat(x)!=1:
        print('Ошибка! Введите число!')
        x=input("Введите элемент массива: ")
x=float(x)
a.append(x)
m=x
k=0
for i in range(N-1):
    x=input("Введите элемент массива: ")
    if isfloat(x)==0:
        while isfloat(x)!=1:
            print('Ошибка! Введите число!')
            x=input("Введите элемент массива: ")
    x=float(x)
    a.append(x)
    
print('Данный массив:',*a)
poiskmax(a)
zero(a,k)