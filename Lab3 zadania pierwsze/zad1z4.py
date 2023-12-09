a = int(input('podaj liczbe '))
b = int(input('podaj liczbe '))


if(a>=b):
    while b<=a:
        if (b % 2 == 1):
            b += 1
            continue
        print(b)
        b+=1
elif b>=a:
    while a <= b:
        if (a % 2 == 1):
            a += 1
            continue
        print(a)
        a += 1

