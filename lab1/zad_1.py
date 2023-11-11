a = int(input(f"Podaj wiek klienta: "))

while a <= 0:
    print(f"Błędny wiek spróbuj jescze raz")
    a = int(input(f"Podaj wiek klienta: "))

if a < 4:
    print(f"Wstęp bezplatany")
elif a >= 4 and a<=18:
    print(f"Wstęp 10zł")
elif a>18:
    print(f"Wstęp 20zł")

