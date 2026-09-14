import random

# Tehtävä 1

def heitto():   
    return random.randint(1,6)

silmäluku = 0

while silmäluku < 6:
    silmäluku = heitto()
    print(silmäluku)


# Tehtävä 2


def heitto(tahko):
    return random.randint(1, tahko)

silmäluku = 0
max_silmäluku = int(input("Anna tahkojen lukumäärä: "))

while silmäluku < max_silmäluku:
    silmäluku = heitto(max_silmäluku)
    print(silmäluku)


# Tehtävä 3

def määrä(gallonaa):
    return gallonaa * 3.78
    
bensiini = 0
gallona_lkm = float(input("Anna gallonat: "))

while gallona_lkm > 0:
    bensiini = määrä(gallona_lkm)
    print(f"{gallona_lkm} gallonaa on {bensiini} litraa")
    gallona_lkm = float(input("Anna gallonat: "))
    if gallona_lkm < 0:
        break

# Tehtävä 4

def summa(kokonaisluvut):
    return sum(kokonaisluvut)

kokonaisluku = [1, 2, 3, 4, 5, 6]
luvut = summa(kokonaisluku)
print(luvut)


# Tehtävä 5

def funktio(lista):
    return [luku for luku in lista if luku % 2 == 0]

kokonaisluku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parilliset = funktio(kokonaisluku)
print(kokonaisluku)
print(parilliset)


# Tehtävä 6
import math

def funktio(halkaisija, hinta):
    return (hinta / (math.pi * ((halkaisija / 2)**2)))
    
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))
yksikköhinta1 = funktio(halkaisija1,hinta1)
halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))
yksikköhinta2 = funktio(halkaisija2,hinta2)

if yksikköhinta1 < yksikköhinta2:
    print("Ensimmäinen pizza antaa enemmän vastinetta rahalle.")
elif yksikköhinta1 > yksikköhinta2:
    print("Toinen pizza antaa enemmän vastinetta rahalle.")
else:
    print("Pzzat ovat yhtä edullisia")
    