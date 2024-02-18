import math

def pole_troj(bok1, bok2, kat):
    if bok1 <= 0 or bok2 <= 0 or kat <= 0:
        print("Długości boków muszą być dodatnie.")
        return "błąd"

    if bok1 + bok2 <= kat:
        print("Trójkąt nie istnieje.")
        return "błąd"

    if kat >= 90:
        print("Trójkąt nie jest ostrokątny.")
        return "błąd"

    kat_rad = math.radians(kat)


    pole = 0.5 * bok1 * bok2 * math.sin(kat_rad)

    return "pole: ",pole


bok1 = float(input("Podaj długość pierwszego boku: "))
bok2 = float(input("Podaj długość drugiego boku: "))
kat = float(input("Podaj szerokość kąta ostrego w stopniach: "))

print(pole_troj(bok1, bok2, kat))
