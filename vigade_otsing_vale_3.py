
from random import *

def vahetus(a, b):
    """
    Vahetab kahe arvu väärtused omavahel.
    Tagastab uued väärtused järjekorras (a, b).
    """
    abi = a
    a = b
    b = abi
    return a, b


def generaator(n, loend, a, b):
    """
    Genereerib n juhuslikku täisarvu vahemikus a kuni b
    ja lisab need antud loendisse.
    """
    for i in range(n):
        loend.append(randint(a, b))   # parandatud: loend(append(...)) -> loend.append(...)


def jagamine(loend, p, n, nol):
    """
    Jagab loendi elemendid positiivseteks, negatiivseteks ja nullideks.
    Tulemus lisatakse vastavatesse loenditesse p, n ja nol.
    """
    for el in loend:
        if el > 0:
            p.append(el)              # parandatud: p(append(...)) -> p.append(...)
        elif el < 0:                  # parandatud: elif:: -> elif el < 0:
            n.append(el)
        else:
            nol.append(el)


def keskmine(loend):
    """
    Arvutab loendis olevate arvude aritmeetilise keskmise.
    Kui loend on tühi, tagastatakse 0.
    """
    n = len(loend)
    if n == 0:
        kesk = 0
    else:
        summa = 0                     # parandatud: muutuja 'sum' asendatud sõnaga 'summa'
        for i in loend:
            summa += i
        kesk = round(summa / n, 2)    # parandatud: keskmise arvutus oli tsükli sees
    return kesk


def lisamine(loend, el):
    """
    Lisab uue elemendi loendisse ja sorteerib selle.
    """
    loend.append(el)
    loend.sort()                      # parandatud: loend(sort()) -> loend.sort()


def arvud_loendis():
    """
    Põhifunktsioon, mis juhib kogu programmi tööd:
    - küsib kasutajalt andmed,
    - genereerib juhuarvud,
    - jagab need gruppidesse,
    - leiab keskmised
    - ja väljastab lõpptulemuse.
    """
    print("Andmed:")
    n = abs(int(input("Mitu täisarvu genereerime loendisse? => ")))
    mini = int(input("Sisesta vahemiku minimaalne arv => "))
    maxi = int(input("Sisesta vahemiku maksimaalne arv => "))

    if mini >= maxi:
        mini, maxi = vahetus(mini, maxi)

    s = []
    generaator(n, s, mini, maxi)

    print("\nTulemused:")
    print("Saadud loend vahemikus", mini, "kuni", maxi, ":", s)

    s.sort()
    print("Sorteeritud loend:", s)

    pos = []
    neg = []
    null = []

    jagamine(s, pos, neg, null)

    print("Positiivsed arvud:", pos)
    print("Negatiivsed arvud:", neg)
    print("Nullid:", null)

    kesk = keskmine(pos)
    print("Positiivsete keskmine:", kesk)
    lisamine(s, kesk)

    kesk = keskmine(neg)
    print("Negatiivsete keskmine:", kesk)
    lisamine(s, kesk)

    print("\nLisame keskmised algsesse massiivi ja sorteerime:")
    s.sort()
    print(s)


# --- Programmi käivitamine ---
arvud_loendis()



### 🧩 Programmi töö näide:

# Andmed:
# Mitu täisarvu genereerime loendisse? => 10
# Sisesta vahemiku minimaalne arv => -5
# Sisesta vahemiku maksimaalne arv => 5

# Tulemused:
# Saadud loend vahemikus -5 kuni 5 : [-2, 3, 0, 5, -5, 2, -1, 0, 4, -3]
# Sorteeritud loend: [-5, -3, -2, -1, 0, 0, 2, 3, 4, 5]
# Positiivsed arvud: [2, 3, 4, 5]
# Negatiivsed arvud: [-5, -3, -2, -1]
# Nullid: [0, 0]
# Positiivsete keskmine: 3.5
# Negatiivsete keskmine: -2.75

# Lisame keskmised algsesse massiivi ja sorteerime:
# [-5, -3, -2.75, -2, -1, 0, 0, 2, 3, 3.5, 4, 5]

