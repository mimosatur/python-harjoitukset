import random

# Tehtävä 1

luku = 1

while luku <= 1000:
    # onko luku kolmella jaollinen, jos on niin printtaa
    if luku % 3 == 0:
        print(luku)
    luku += 1

# Tehtävä 2

# 1 tuuma = 2,54 cm

tuuma = float(input("Anna tuumat: "))

senttimetri = tuuma * 2.54

while tuuma >= 0:
    print(f"{tuuma} tuumaa on senttimetreinä {float(senttimetri)} cm")
    tuuma = float(input("Anna tuumat: "))
    senttimetri = tuuma * 2.54
    if tuuma < 0:
        tuuma -= 1


# Tehtävä 3

luku = float(input("Anna luku: "))

while luku != (""):
    luku = float(input("Anna luku: "))
    if luku == (""):
        luku += 1


# Tehtävä 4

luku = random.randint(1,10)

arvaus = int(input("Arvaa luku 1 ja 10 välillä: "))

while arvaus < luku:
    print("Liian pieni arvaus")
    arvaus = int(input("Arvaa uudestaan: "))
    if arvaus > luku:
        print("Liian suuri arvaus")
        arvaus = int(input("Arvaa uudestaan: "))
    elif arvaus == luku:
        print("Oikein")


# Tehtävä 5


arvaus1 = str(input("Anna käyttäjätunnus: "))
arvaus2 = str(input("Anna salasana: "))

oikea_käyttäjätunnus = "python"
oikea_salasana = "rules"

while arvaus1 != oikea_käyttäjätunnus and arvaus2 != oikea_salasana:
    arvaus1 = str(input("Anna käyttäjätunnus uudelleen: "))
    arvaus2 = str(input("Anna salasana uudelleen: "))
    if arvaus1 != oikea_käyttäjätunnus or arvaus2 != oikea_salasana:
        arvaus1 = str(input("Anna käyttäjätunnus uudelleen: "))
        arvaus2 = str(input("Anna salasana uudelleen: "))
    elif arvaus1 == oikea_käyttäjätunnus and arvaus2 == oikea_salasana:
        arvaus1 = str(input("Anna käyttäjätunnus uudelleen: "))
        arvaus2 = str(input("Anna salasana uudelleen: "))
    elif arvaus1 != oikea_käyttäjätunnus and arvaus2 != oikea_salasana < 5:
        print("Pääsy evätty")

print("Tervetuloa!")



