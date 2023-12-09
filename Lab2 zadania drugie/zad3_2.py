a = int(input('podaj liczbe '))
for i in range(a):
    for c in range(i+1):
        print("x",end=" ")
    print("")


n=1
for i in range(a):
    print( a* " " +"x"*n)
    a=a-1
    n=n+2