from os import replace
from colorama import *
from random import *
sõnad = [
    "kevad",
    "sügis",
    "päike",
    "ratas",
    "laine",
    "klaas",
    "paber",
    "tants",
    "ilves",
    "põder",
    "tänav",
    "tehas",
    "tunne",
    "sõber",
    "kirik",
    "teema",
    "kirst",
    "kaart"
]
pos=randint(0, len(sõnad) - 1) # juhuslik positsioon 
sõna=sõnad[pos] # juhuslik sõna
print(sõna)
sõna_list=list(sõna) # "päike" -> ["p","ä","i","k","e"]
print(sõna_list)
sõna_=""
for t in sõna:
    t=t.replace(t, "_") # asenda täht _-ga
    sõna_+=t
print(sõna_)
katseid=6 # katsete arv
print("Arva 5-täheline eestikeelne sõna.")
print("Sul on", katseid, "katset.\n")
while katseid>0:
    täht=input("Sisesta täht: ")