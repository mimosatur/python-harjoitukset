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

print(f"{tuuma} tuumaa on senttimetreinä {senttimetri} cm")