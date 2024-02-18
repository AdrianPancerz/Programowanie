import time

def pozostaly_czas():
    sekunda = int(input("Podaj czas w sekundach : "))

    while sekunda > 0:
        print("Pozostało", sekunda, "sekund")
        time.sleep(1)
        sekunda -= 1

    print("Koniec")



pozostaly_czas()