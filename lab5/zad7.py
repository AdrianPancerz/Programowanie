import random

def srednia(nr):
    ilosc = 1
    for i in nr:
        ilosc *= i
    return ilosc ** (1 / len(nr))


pocz = int(input("początek przedziału: "))
koniec = int(input("koniec przedziału: "))


krotka = tuple(random.randint(pocz, koniec) for _ in range(10))

print("Losowa krotka:", krotka)



print("Średnia geometryczna krotki:", srednia(krotka))