from Teema5Moodul import *
#1
for x in range(6): 
    arv1=float(input("Sisesta esimene arv: "))
    arv2=float(input("Sisesta teine arv: "))
    tehe=input("Sisesta tehe (+ - * /): ")
    v=arithmetic(arv1,arv2,tehe)
    print(v)
#2
aasta=int(input("Sisesta aasta: "))
print(f"{aasta} on {is_year_leap(aasta)} kui True siis liigaasta, kui False siis tavaline")

#3
külg=float(input("Sisesta ruudu külje pikkus: "))
P, S, D = square(külg)
print(f"Ruudu ümbermõõt: {P}, pindala: {S}, diagonaal: {D}")
from random import randint
#4
for i in range(10):
    kuu=randint(-50,50)
    print(f"Kuu number: {kuu}, aastaaja on: {season(kuu)}")

#5
while True:
    try:
        summa=float(input("Sisesta summa eurodes: "))
        if summa>0:
            break
        else:
            print("Summa peab olema positiivne arv.")
    except:
        print("Palun sisesta korrektne arv.")
while True:
    try:
        aastad=int(input("Sisesta summa eurodes: "))
        if aastad>0:
            break
        else:
            print("Summa peab olema positiivne arv.")
    except:
        print("Palun sisesta korrektne arv.")
lsumma=bank(summa,aastad)
print(f"Pärast {aastad} aastat on kontol summa: {lsumma:.3f} eurot.")