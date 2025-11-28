#1
# Kirjuta funktsioon arithmetic, mis võtab 3 argumenti: 
# esimesed 2 on arvud, kolmas on tehe, mis nende vahel tuleb teha. 
# Kui kolmas argument on +, liida need; kui -, lahuta; kui *, 
# korruta; kui /, jaga (esimene teisega). 
# Kõigil muudel juhtudel tagasta string "Tundmatu tehe".
def arithmetic(arv1:float,arv2:float,tehe:str)->any:
    """Lihtne kalkulaator.
    + - liitmine,
    - - lahutamine,
    * - korrutamine,
    / - jagamine.
    Muul juhul tagastab "Tundmatu tehe".
    :param float a: Esimene arv.
    :param float b: Teine arv.
    :param str tehe: Tehe, mis tuleb teha.
    :rtype: float või str
    """
    if tehe in ["+","-","*","/"]:
        if tehe=="/" and arv2==0:
            vastus="DIV/0"
        else:
            vastus=eval(f"{arv1}{tehe}{arv2}")
    else:
        vastus="Tundmatu tehe"
    return vastus
#2
#Kirjuta funktsioon is_year_leap, 
#mis võtab ühe argumendi — aasta, ja tagastab True, 
#kui aasta on liigaasta, ja False muul juhul.
def is_year_leap(aasta:int)->bool:
    """Kontrollib, kas antud aasta on liigaasta.
    :param int aasta: Aasta arvuna.
    :rtype: bool
    """
    if (aasta % 4 == 0 and aasta % 100 != 0) or (aasta % 400 == 0):
        return True
    else:
        return False
#3
#Kirjuta funktsioon square, mis võtab ühe argumendi
# — ruudu külje pikkuse, ja tagastab kolm väärtust: 
#ruudu ümbermõõt, pindala ja diagonaal.   
def  square(külg:float)->tuple:
    """Arvutab ruudu ümbermõõdu, pindala ja diagonaali.
    :param float külg: Ruudu külje pikkus.
    :rtype: tuple
    """
    ümbermõõt=4*külg
    pindala=külg**2
    diagonaal=round((külg*(2**0.5)),2)
    return ümbermõõt,pindala,diagonaal  
#4
# Kirjuta funktsioon season, mis võtab ühe argumendi — kuu number (1 kuni 12), 
# ja tagastab selle kuu vastava aastaaja 
# (talv, kevad, suvi või sügis).

def season(kuu:int)->str:
    """Tagastab kuu numbri põhjal aastaaja.
    :param int kuu: Kuu number (1-12).
    :rtype: str
    """
    if kuu in [12,1,2]:
        s="talv"
    elif kuu in [3,4,5]:
        s="kevad"
    elif kuu in [6,7,8]:
        s="suvi"
    elif kuu in [9,10,11]:
        s="sügis"
    else:
        s="!!!"
    return s

#5
# Kasutaja teeb hoiuse summas a eurot years aastaks 10% aastaintressiga 
# (igal aastal suureneb hoiusumma 10%, 
#  ka intressile arvestatakse järgmise aasta intress).
# Kirjuta funktsioon bank, mis võtab argumendid a ja years, 
# ning tagastab lõppsumma kasutaja kontol.

def bank(summa:float,aastad:int)->float:
    """Arvutab hoiuse lõppsumma koos intressidega.
    :param float summa: Hoiuse algsumma eurodes.
    :param int aastad: Hoiuse kestvus aastates.
    :rtype: float
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa
