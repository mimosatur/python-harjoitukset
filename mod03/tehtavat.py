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

a = float(input("Anna leiviskät:\n"))
b = float(input("Anna naulat:\n"))
c = float(input("Anna luodit:\n"))

kilogrammaa = (a * 8.5) + (b * 0.425) + (c * 0.0133)
grammaa = (a * 8500) + (b * 425) + (c * 13.3)

print(f"Massa nykymittojen mukaan:\n{int(kilogrammaa)} kilogrammaa ja {grammaa} grammaa")

# tehtävä 6

luku = random.randint(0,9)
luku2 = random.randint(0,9)
luku3 = random.randint(0,9)

print(f"{luku} {luku2} {luku3}")
print(f"{random.randint(1,6)} {random.randint(1,6)} {random.randint(1,6)} {random.randint(1,6)}")