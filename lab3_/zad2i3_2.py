listazakup = {"Czekolada": 8,"stek":70,"Hugo":20}
suma = (listazakup.values())
print(listazakup)
suma = sum(suma)
print('suma: ',suma)
#zad3
rachunek={"Wrzesien":50,"pazdiernik":65,"listopad":57}

suma = rachunek.values()
sumaa = sum(suma)
print('Suma',sumaa)
print('Maksymalna wartośc: ',(max(rachunek.values())))
print('Minimalna Wartosć',(min(rachunek.values())))
x = int(len(rachunek))
srednia = sumaa/x
print('Średnia wartość: ',srednia)

ostatni = rachunek["listopad"]
if(srednia>ostatni):
    print("Zacznij oszczędzać")
else:print('Jesteś bezpieczny')