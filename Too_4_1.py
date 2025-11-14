# 1 Sisesta sõna või lause.
# Loenda:
#     mitu täishäälikut 
#     mitu kaashäälikut 
#     kui sisestati lause – loenda ka tühikud ja kirjavahemärgid 
import string
t=["a","e","u","o","i","ü","ö","õ","ä"]
k=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","š","z","ž","t","v","w","x","y"]
m=string.punctuation # %&'()*+,-./:;<=>?@[\]^_`{|}~
sõne=input("Sisesta sõna või lause: ")
sõne=sõne.lower()
täishäälikud=0
kaashäälikud=0
muu=0
for täht in sõne:
    if täht in t:
        täishäälikud+=1
    elif täht in k:
        kaashäälikud+=1
    else:
        muu+=1
print("Täishäälikuid:", täishäälikud)
print("Kaashäälikuid:", kaashäälikud)
print("Tühikud ja kirjavahemärgid:", muu)

#4
indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa"," Läänemaa, Hiiumaa, Saaremaa"]
while True:
    try:
        pindex=int(input("Sisesta postiindeks (5-kohaline): ")) #37521
        if len(str(pindex))==5:
            break
        else:
            print("Postiindeks peab olema 5-kohaline!")
    except :
        print("Vigane andmetüüp")
pindex_list=list(pindex) # pindex=37521 -> list("37521")=["3","7","5","2","1"]
esimne_number=int(pindex_list[0]) # pindex_list[0]="3" -> int("3")=3
print(f"Postiindeks {pindex} asub piirkonnas: {indexid[esimne_number-1]}")
if esimne_number in [0,1,2,8]:
    print("Mine merre")
else:
    print("Mine metsa")

# 6 
#Leia loendi suurim arv, jaga see loendi pikkusega ja asenda see tulemusena.
from random import randint
arvud=[]
mitu=randint(5,15)
for i in range(mitu):
    arvud.append(randint(1,100))
print("Algne loend:", arvud)
maks=max(arvud)
pikk=len(arvud)
asendus=round(maks/pikk,2)
index_maks=arvud.index(maks)
arvud[index_maks]=asendus
print("Uus loend:", arvud)

# 7
#Sorteeri nimekiri numbreid absoluutväärtuse järgi,kasvavalt  või kahanevalt 

arvud.clear()
for i in range(10):
    arvud.append(randint(-50,50))
print("Algne loend:", arvud)
valik=input("Kas soovid sorteerida kasvavalt (k) või kahanevalt (h)? ")
if valik.lower()=="k":
    arvud.sort(key=abs)
else:
    arvud.sort(key=abs)
    arvud.reverse()

print("Sorteeritud absoluutväärtuse järgi:", arvud)