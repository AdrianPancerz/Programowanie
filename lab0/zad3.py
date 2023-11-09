import random
z = int(input(f"Podaj pierwszy bok: "))
x = int(input(f"Podaj drugi bok: "))

pole = z*x
obw = (2*z)+(2*x)
if(z==x):
    print(f"Pole kwadratu to :{pole}")
    print(f"Obwód kwadratu to :{obw}")
if(z!=x):
    print(f"Pole Prostokąta to :{pole}")
    print(f"Obwód Prostokąta to :{obw}")
