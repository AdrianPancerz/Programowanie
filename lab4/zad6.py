import math
def polrtrj(a,b,c):
    if (a + b <= c or a + c <= b or c + b <= a):
        print("nieprawidłowe dane")
    elif(a==b and a==c and b==c):
        h = (a*math.sqrt(3))/2
        pole = a*h/2
        print('Pole trójkąta równobocznego to :', pole)

    elif(a!=c and b!=c and c!=b and b!=a):
        p = (a+b+c)/2
        pole1 = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("Pole trójkąta różnobocznego to :", pole1)

    elif(a==b or b==c or c==a):
        if(a+b<c or a+c<b or c+b<a):
            print("nieprawidłowe dane")
        else:
            if(a==b):
                h1 = math.sqrt(a*a - math.pow(c/2,2))
                pol = c*h1/2
                print("Pole trójąkąta równoramiennego to:",pol)
            if (a==c):
                h1 = math.sqrt(a * a - math.pow(b / 2, 2))
                pol = b*h1/2
                print("Pole trójąkąta równoramiennego to:", pol)
            if (c==b):
                h1 = math.sqrt(c * c - math.pow(a / 2, 2))
                pol = a*h1/2
                print("Pole trójąkąta równoramiennego to:", pol)

polrtrj(6,6,11)