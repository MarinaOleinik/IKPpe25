#Ülesanne1
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, 
# kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”

# print("Tere, maailm!")
# nimi = input("Mis su nimi on? ").capitalize()
# print(f"Tere, maailm! Tervitan sind {nimi}")
# vanus = int(input("Kui vana sa oled? "))
# print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.".upper())

#Ülesanne2
# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 166.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.

vanus=18 #täisarv
print(f"Muutuja vanus on tüübilt {type(vanus)}")
eesnimi="Jaak" #sõne
print(f"Muutuja eesnimi on tüübilt {type(eesnimi)}")
pikkus=166.5 #ujukomaarv
print(f"Muutuja pikkus on tüübilt {type(pikkus)}")
kas_käib_koolis=True #loogikaväärtus
print(f"Muutuja kas_käib_koolis on tüübilt {type(kas_käib_koolis)}")

#Ülesanne3
# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). 
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, 
# kui palju komme laual nüüd on. 

from random import *
kommide_arv=randint(10, 100)
print(f"Laual on {kommide_arv} kommi.")
võetud_kommide_arv=int(input("Mitu kommi sa soovid laualt ära võtta? "))
if võetud_kommide_arv>kommide_arv:
    print("Laual pole nii palju komme.")
else:
    kommide_arv-=võetud_kommide_arv
    print(f"Nüüd on laual {kommide_arv} kommi.")

#Ülesanne 4
# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning 
# teatab selle peale puu läbimõõdu.
C=float(input("Sisesta puu ümbermõõt meetrites: "))
d=C/3.14
print(f"Puu läbimõõt on {d:.2f} meetrit.")




print("Saame tutavaks!")
nimi = input("Mis su nimi on? ").capitalize() # sõne
print("Tere, " + nimi + "!")
vanus = int(input("Kui vana sa oled? ")) # täisarv
print("Oled " + str(vanus) + " aastat vana.")
print(f"Järgmise aasta sa oled {vanus + 1} aastat vana.")
