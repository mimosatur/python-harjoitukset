import math
import random


# tehtävä 1

nimi = input("Mika on nimesi: ")
print(f"Terve, {nimi}!")

# tehtävä 2
 
r = float(input("Anna säde niin lasken ympyrän pinta-alan: "))
# r = float(r)
# ympyrän pinta-ala: A = pi * r'2
A = math.pi * r ** 2
print(f"ympyrän pinta-ala on {A:.2f} yksikköä")


# tehtävä 3

a = float(input("Anna suorakulmion kanta: "))
b = float(input("Anna suorakulmion korkeus: "))

# suorakulmion piiri: p = 2a + 2b
p = 2 * (a + b) 
# suorakulmion pinta-ala: A = a * b
A = a * b

print(f"Suorakulmion piiri on: {p:.2f} ja pinta-ala {A:.2f}")
print(f"Suorakulmion piiri on: {p:.2f} ja pinta-ala {(a*b):.2f}")

# tehtävä 4

a = float(input("Anna ensimmäinen luku: "))
b = float(input("Anna toinen luku: "))
c = float(input("Anna kolmas luku: "))

summa = a + b + c
tulo = a * b * c
keskiarvo = (a + b + c) / 3

print(f"Lukujen summa: {summa}")
print(f"Lukujen tulo: {tulo}")
print(f"Lukujen keskiarvo: {keskiarvo}")

# tehtävä 5

leiviska_lkm = float(input("Anna leivisköjen määrä:\n"))
naula_lkm = float(input("Anna naulojen määrä:\n"))
luoti_lkm = float(input("Anna luotien määrä:\n"))

# lasketaan leiviskät mukaan nauloihin
naula_lkm = leiviska_lkm * 20 + naula_lkm
# lasketaan naulat mukaan luoteihin
luoti_lkm = naula_lkm * 32 + luoti_lkm

# välitarkastus, että kaikki toimii
# print(f"Koko massa luoteina: {luoti_lkm}")

massa_g = luoti_lkm * 13.3

print(f"Massa nykymittojen mukaan:\n{int(massa_g // 1000)} kilogrammaa {massa_g % 1000:.2f} grammaa")

# tehtävä 6

luku = random.randint(0,9)
luku2 = random.randint(0,9)
luku3 = random.randint(0,9)

print(f"{luku} {luku2} {luku3}")
print(f"{random.randint(1,6)} {random.randint(1,6)} {random.randint(1,6)} {random.randint(1,6)}")