# 1. Juku
# a Kui eesnimi on Juku siis lähme Jukuga kinno. 
# Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.
# b Lisa valiku, kus Juku vanuse alusel otsustate
#  mis pilet talle vaja osta. 
#  (Tee kontroll, kas sisestatud arv on täisarv)
#     <6 aastad  - tasuta
#     6-14 - lastepilet
#     15-65 - täispilet
#     >65 - sooduspilet
#     <0 ja >100 viga andmetega
nimi=input("Mis su nimi on? ")
if nimi=="JUKU":
    print("Lähme Jukuga kinno!")
    try:
        vanus=int(input("Kui vana sa oled? "))
        if vanus<0 or vanus>100:
            print("Viga andmetega!")
        elif vanus<6:
            print("Pilet on tasuta!")
        elif 6<=vanus<=14:
            print("Osta lastepilet!")
        elif 15<=vanus<=65:
            print("Osta täispilet!")
        else:
            print("Osta sooduspilet!")
    except:
        print("Viga. Sisesta täisarv!")



# kontroll kas pos või neg arv

try:
    arv=int(input("Sisesta suvaline täisarv: "))
    if arv>0:
        print("Positiivne")
    elif arv<0:
        print("Negatiivne")
    else:
        print("See on =0")
except:
    print("Viga. Sisesta arv!")