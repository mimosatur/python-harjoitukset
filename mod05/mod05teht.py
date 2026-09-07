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

luku = input("Anna luku: ")

if luku != "":
    luku = int(luku)
    pienin_luku = luku
    suurin_luku = luku

    while True:
        luku = input("Anna luku: ")

        if luku == "":
            break

        luku = int(luku)

        if luku < pienin_luku:
         pienin_luku = luku
        if luku > suurin_luku:
         suurin_luku = luku

    print(f"Pienin luku on {pienin_luku} ja suurin luku on {suurin_luku}")

      


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

max_yritykset = 5
yritykset = 0


while True:
    arvaus1 = input("Anna käyttäjätunnus: ")
    arvaus2 = input("Anna salasana: ")
    yritykset += 1
        
    if arvaus1 == "python" and arvaus2 == "rules":
        print("Tervetuloa!")
        break
    elif yritykset > max_yritykset:
        print("Pääsy evätty")
        break

