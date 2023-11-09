
import random
spalanie = float(input(f"średnie spalanie w l na 100km: "))
los = random.randint(1, 1000)

print(f"Trasa: {los}km")

s = los*spalanie/100
print(f"Zużycie paliwa to: {s} l")
cena = s*6.5

print(f"Koszt podrózy to:  {cena} zł")





