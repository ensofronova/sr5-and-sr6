def isint(x):
    try:
        int(x)
        return 1
    except ValueError:
        return 0

def is28(x):
    if x=='2' or x=='8':
        return 1
    else:
        return 0

a=input('Введите число: ')
if isint(a)==0:
    while isint(a)!=1:
        print('Ошибка! Введите число!')
        a=input("Введите число: ")
a=int(a)

n=input('Введите систему счисления 2 или 8: ')
if (isint(n)==0) or (is28(n)==0):
    while (isint(n)!=1) or (is28(n)!=1):
        print('Ошибка! Введите 2 или 8!')
        n=input('Введите систему счисления 2 или 8: ')
n=int(n)

c=''
o=a
while a>0:
    b=a%n
    c+=str(b)
    a=a//n
    
print('Число',o,'в системе счисления',n,'равно',c[::-1])