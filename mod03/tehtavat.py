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
