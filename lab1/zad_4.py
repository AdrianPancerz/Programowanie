import math
print("Równanie kwadratowe")

print("Podaj trzy liczby")
a = int(input(f"współczynnik a : "))
b = int(input(f"współczynnik b : "))
c = int(input(f"współczynnik c : "))


delta = b**2 - (4 *a*c)

if(delta>0):
    x1 = ((b*-1)+math.sqrt(delta))/(2*a)
    x2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
    print(f"Delta dodatnia dwa rozwiązania : {round(x1,2)}, {round(x2,2)}")
elif(delta == 0):
    x = (b * -1)/(2*a)
    print(f"Delta 0 jedno rowziązanie : {x}")
else:
    print(f"Brak rozwiązań delta ujemna")


