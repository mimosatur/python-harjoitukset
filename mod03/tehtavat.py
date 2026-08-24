import math
import random

print("Hello, world!")

# tehtävä 1

nimi = input("Anna nimesi: ")
print(f"Terve, {nimi}!")

# tehtävä 2

# ympyrän pinta-ala: A = pi * r'2 
r = float(input("Anna säde niin lasken ympyrän pinta-alan"))
# r = float(r)
print(r)
A = math.pi * r ** 2
print(f"ympyrän pinta-ala on {A:.2f}")