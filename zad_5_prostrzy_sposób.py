a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 2nd number: '))

tab = [a,b,c]
naj= 0
srednia = 0
mala = 0
dod = 0
d = 0
for x in tab:
    if(d==0):
        naj = x

    if(d==1):
        if(x>naj):
            dod = naj
            naj = x
            srednia = dod
        elif(x<naj):
            srednia = x
    if(d==2):
        if(x>naj):
            dod=srednia
            srednia = naj
            naj = x
            mala = dod
        elif(srednia>x):
            srednia =srednia
            mala = x
        elif(srednia<x):
            dod = srednia
            srednia = x
            mala = dod
    d+=1


print(mala, srednia, naj)

