import math
print("Pole Trójkąta")

bok1 = int(input(f"Podaj bok a: "))
bok2 = int(input(f"Podaj bok b: "))
bok3 = int(input(f"Podaj bok c: "))
wynik = (bok1+bok2+bok3)/2
P = math.sqrt(wynik*((wynik-bok1)*(wynik-bok2)*(wynik-bok3)))
print("Pole trójkata to : ",P )
