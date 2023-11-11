print("Kalkulator")
print(f"Jaką operacje chcesz wykonać? ")
print(f"1) Dodawanie")
print(f"2) Odejmowanie")
print(f"3) Mnożenie")
print(f"4) Dzielenie")
print(f"5) Potęgowanie")
oper = int(input(f"Wybierz operacje: "))

while oper <= 0 or oper > 5:
    print(f"Błędnna opcja sróbuj ponownie")
    oper = int(input(f"Wybierz operacje: "))

print("Podaj dwie liczby")
liczba1 = int(input(f"Argument 1: "))
liczba2 = int(input(f"Argument 2: "))

if(oper == 1):
    print(f"Wynik: ", liczba1 + liczba2)
elif(oper == 2):
    print(f"Wynik: ", liczba1 - liczba2)
elif(oper == 3):
    print(f"Wynik: ", liczba1 * liczba2)
elif(oper == 4):
    print(f"Wynik: ", liczba1/liczba2)
elif(oper == 5):
    print(f"Wynik: ", liczba1**liczba2)

