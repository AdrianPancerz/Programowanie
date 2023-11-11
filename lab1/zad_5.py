import math


print("Podaj trzy liczby")
a = int(input(f" a : "))
b = int(input(f" b : "))
c = int(input(f" c : "))


if(a>b and a>c):
    if(b>c):
        print(f"{c},{b},{a}")
    elif(c>b):
        print(f"{b},{c},{a}")
if(b>a and b>c):
    if(a>c):
        print(f"{c},{a},{b}")
    elif(c>a):
        print(f"{a},{c},{b}")
if(c>a and c>b):
    if(a>b):
        print(f"{b},{a},{c}")
    elif(b>a):
        print(f"{a},{b},{c}")
if(a==b and a==c):
    print(f"liczby sa takie same {a},{b},{c}")
if(a==b):
    if(a>c):
        print(f"{c},{b},{a}")
    if(c>a):
        print((f"{a},{b},{c}"))
if(a==c):
    if(a>b):
        print(f"{b},{c},{a}")
    if(b>a):
        print((f"{c},{a},{b}"))
if(c==b):
    if(a>c):
        print(f"{c},{b},{a}")
    if(c>a):
        print((f"{a},{b},{c}"))


