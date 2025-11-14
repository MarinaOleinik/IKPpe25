sõne=input("Palun sisesta sõne: ")
print("Sinu sisestatud sõne on:", sõne)
sõne_list=list(sõne)
valik=int(input("Kas rida või veerg (1-rida, 2-veerg): "))
if valik==2:
    for täht in sõne_list:
        print(täht)
else:
    print("Sõne listina:", sõne_list)

print("1-Elemendi lisamine \n2-Positsioonile lisamine \n3-Eemaldamine \n4-Loendame elemendi \5-Sort \n6-Tühjendus")
valik=int(input("Valik:"))
if valik==1:
    element=input("Sisesta element, mida soovid lisada:")
    sõne_list.append(element) # Lisab uue elemendi listi lõppu
    print("Uus sõne list:", sõne_list)
elif valik==2:
    element=input("Sisesta element, mida soovid lisada:")
    positsioon=int(input("Sisesta positsioon, kuhu soovid lisada (0 kuni {}): ".format(len(sõne_list))))
    if 0 <= positsioon <= len(sõne_list):
        sõne_list.insert(positsioon, element) # Lisab uue elemendi soovitud positsioonile
        print("Uus sõne list:", sõne_list)
    else:
        print("Vigane positsioon!")
elif valik==3:
    valik=int(input("Kas soovid eemaldada elemendi väärtuse (1) või positsiooni (2)? "))
    if valik==1:
        element=input("Sisesta element, mida soovid eemaldada:")
        if element in sõne_list:
            mitu=sõne_list.count(element)
            for x in range(mitu):
                sõne_list.remove(element) # Eemaldab kõik leitud elemendid
                
            # sõne_list.remove(element) # Eemaldab esimest leitud elementi
            print("Uus sõne list:", sõne_list)
        else:
            print("Elementi ei leitud listist!")
    elif valik==2:
        positsioon=int(input("Sisesta positsioon, kust soovid eemaldada (0 kuni {}): ".format(len(sõne_list)-1)))
        if 0 <= positsioon < len(sõne_list):
            eemaldatud_element=sõne_list.pop(positsioon) # Eemaldab elemendi soovitud positsioonilt
            print("Eemaldatud element:", eemaldatud_element)
            print("Uus sõne list:", sõne_list)
        else:
            print("Vigane positsioon!")
    else:
        print("Vigane valik!")
elif valik==4:
    element=input("Sisesta element, mida soovid loendada:")
    arv=sõne_list.count(element) # Loendab, mitu korda element esineb listis
    print("Element '{}' esineb listis {} korda.".format(element, arv))
elif valik==5:
    valik=int(input("Kas soovid sorteerida kasvavalt (1) või kahanevalt (2)? "))
    if valik==1:
        sõne_list.sort() # Sorteerib listi kasvavalt
        print("Sorteeritud sõne list (kasvavalt):", sõne_list)
    elif valik==2:
        sõne_list.sort(reverse=True) # Sorteerib listi kahanevalt
        print("Sorteeritud sõne list (kahanevalt):", sõne_list)
    else:
        print("Vigane valik!")
elif valik==6:
    sõne_list.clear() # Tühjendab kogu listi
    print("Sõne list on nüüd tühi:", sõne_list)