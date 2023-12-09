liczba = int(input("Wprowadź wartość: "))
a = 1
if liczba == 0:
    print("Zero silnia wynosi: 1")
else:
    while liczba >= 1:
        a = a * liczba
        liczba = liczba - 1
    print("Silnia wynosi: ", a)