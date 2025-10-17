# Ülesanne 1
# Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt N(N küsi kasutajalt) korda 
# ja lisab ka tervituse järjekorranumber.
#for



# nime=input("Sisesta oma nimi: ")
# N=int(input("Mitu korda soovid tervitust saada? "))
# for i in range(1, N+1):
#     print(f"Tere, {nime}! See on sinu {i}. tervitus.")

# #while True
# i=1
# while True:
#     print(f"Tere, {nime}! See on sinu {i}. tervitus.")
#     i+=1
#     if i > N: break

# #while tingimusega
# i=1
# while i <= N:
#     print(f"Tere, {nime}! See on sinu {i}. tervitus.")
#     i+=1
#Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
#Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt
#sisestusklahvi.
summa = 0.0
korda = 0

while True:
    arv = input("Sisesta arv: ")
    if arv == "":           # tühja rea puhul lõpetame
        break
    try:
        arv = float(arv)
    except ValueError:
        print("Palun sisesta kehtiv arv või vajuta Enter lõpetamiseks.")
        continue
    summa += arv
    korda += 1
    if korda ==10:
        print("Oled sisestanud 10 arvu, lõpetame.")
        break
print(f"Sisestati {korda} arvu. Kokku: {summa}")