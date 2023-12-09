n = int(input('podaj liczbe n '))
a = int(input('pierwszy wyraz ciagu '))
r = int(input('róznica ciagu '))
w=0
for i in range(1,n+1):
    w = a+(i-1)*r
    print(w)


