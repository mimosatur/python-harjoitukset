# Mod 13 - tiedostonkäsittelyä

# open mitä avataan, as - luodaan muuttuja mikä viittaa tiedostoon(olioon)
# w kertoo millaista tarkoitusta varten avataan tiedosto
#with open("data.txt", "w") as data_tiedosto:
   # data_tiedosto.write("kukkuu")

# datan(tiedon) lukeminen
with open("mod13/intro-teksti.txt") as intro_file:
    print(intro_file.read())

# datan tallentaminen
# tässä tapauksessa tiedoston polku määritellään suhteessa projektin juurikansioon, a = append
with open("mod13/data.txt", "a") as data_tiedosto:
    data_tiedosto.write("kukkuu\n")

# datan lukeminen rivi kerrallaan
with open("mod13/data.txt", "r") as mun_data_tiedosto:
    mun_data = mun_data_tiedosto.readline()
    print("tiedoston data:", mun_data)
    mun_data = mun_data_tiedosto.readline()
    mun_data = mun_data_tiedosto.readline()
    mun_data = mun_data_tiedosto.readline()
    print("tiedoston data:", mun_data)

# Pelaajan tietojen tallennus (suoraan matskusta)

import json

pelaajan_tiedot = {
    "pelaaja": "Matti",
    "taso": 5,
    "varusteet": ["miekka", "kilpi", "haarniska"]
}
with open("mod13/save.json", "w") as tiedosto:
    json.dump(pelaajan_tiedot, tiedosto)

with open("mad13/save.json", "r") as tiedosto:
    data_luettu = json.load(tiedosto)
print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, varusteet: {data_luettu['varusteet']}")