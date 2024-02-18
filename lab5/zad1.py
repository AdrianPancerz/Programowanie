import random

szczesliwy_nr = random.randint(1, 100)
print("Szczęśliwy numerek w grupie to:", szczesliwy_nr)

roczniki = [2001, 2002, 2000, 1998, 1995]


szczesliwy_rocznik = random.choice(roczniki)
print("Szczęśliwy rocznik to:", szczesliwy_rocznik)


numery_totolotka = list(range(1, 50))
wylosowane_numery = random.sample(numery_totolotka, 6)
print("Wylosowane numery Totolotka:", wylosowane_numery)
