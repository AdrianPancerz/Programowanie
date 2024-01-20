def bmi1(waga, wzrost):
    if(waga>0 and wzrost>0 and wzrost<300 and waga<350):

        x = (waga / (wzrost * wzrost)) * 10000
        print("Twoje bmi:",x)
        if x < 18.5:
            print('Niedowaga - zakres < 18.5')
        if x >= 18.5 and x < 25:
            print("Waga prawidłowa - zakres od 18.5 do 25")
        if x >= 25 and x < 30:
            print('Nadwaga - zakres od 25 do 30')
        if x >= 30:
            print('Otyłość - zakres od 30')
    else:
        print("Nieprawidłowe dane")


bmi1(80, 180)