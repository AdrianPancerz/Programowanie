import random

def gra():
    print("Zgadywanie liczby")

    while True:
        try:
            dolny = int(input("Podaj dolny zakres losowania: "))
            gorny = int(input("Podaj górny zakres losowania: "))
            if dolny >= gorny:
                print("Dolny zakres musi być mniejszy niż górny zakres.")
                continue
            break
        except ValueError:
            print("Podano nieprawidłową wartość. Podaj liczbę.")

    liczba = random.randint(dolny, gorny)
    liczba_prob = 3

    print(f"Zgadnij liczbę z zakresu od {dolny} do {gorny}, Masz 3 próby.")


    while liczba_prob > 0:
        try:
            propozycja = int(input("Podaj swoją liczbe: "))


            if propozycja < dolny or propozycja > gorny:
                print("Zły zakres")
                continue

            if propozycja == liczba:
                print("Zgadłeś liczbę!")
                break
            elif propozycja < liczba:
                print("Za mało!")
            else:
                print("Za dużo!")

            liczba_prob -= 1
            print(f"Pozostało Ci {liczba_prob} prób.")

            if liczba_prob == 0:
                print(f"Koniec gry ,wylosowana liczba to {liczba}.")


        except ValueError:
            print("Podano nieprawidłową wartość. Podaj liczbę.")



gra()