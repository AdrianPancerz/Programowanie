import random
i=0
lista=[]
łańcuch = ""
dlugosc = int(input("Podaj maksymalna długość łancucha "))
ilosc = int(input("Podaj ilosc "))
s = int(input("Podaj długośc ciągów znaków do sprawdzenia"))

x = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
while(i<ilosc):
        a = random.randrange(1, dlugosc)
        łańcuch = "".join(((random.sample(x, a))))
        lista.append(łańcuch)
        i+=1;

print(lista)

krotka = tuple(lista)
print(krotka)
ilośc_zanków = 0
litera_k = 0
litera_kt = 0
ilość_dłu = 0
for n in krotka:
    ilośc_zanków = ilośc_zanków + len(n)
    if(len(n)>s):
        ilość_dłu+=1
    if str('kt') in str(n):
        litera_kt +=1
    for c in n:
        if(c=="k"):
            litera_k+=1



print("Ilość zanków: ",ilośc_zanków)
print("Ilość znaków K: ",litera_k)
print("Ilość znaków kt: ",litera_kt)
print("Ilość ciągów dłuższych: ",ilość_dłu)
