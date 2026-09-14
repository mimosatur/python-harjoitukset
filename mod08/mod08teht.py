# Tehtävä 1

jarjestysnumero = int(input("Anna kuukauden numero (1-12): "))
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
vuodenaika = vuodenajat[jarjestysnumero - 1]
print(f"{jarjestysnumero}. kuukausi on {vuodenaika}")


# Tehtävä 2

nimet = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    elif nimi not in nimet:
        print("Uusi nimi")
        nimet.add(nimi)

print(nimet)

# Tehtävä 3

lentoasemat = {
        "EFHK": "Helsinki-Vantaa",
        "LFPB": "Paris-Le Bourget",
        "EGLL": "London Heathrow",
}
print()
while True:
    print("Haluatko syöttää uuden lentoaseman (a), hakea jo syötetyn lentoaseman tiedot (b) vai lopettaa (c)?")
    valinta = input("Syötä valintasi (a, b tai c): ")
    if valinta == "a":
        icao_lisays = input("Anna lentoaseman ICAO-koodi: ")
        nimi_liasys = input("Anna lentoaseman nimi: ")
        lentoasemat[icao_lisays] = nimi_liasys
        
    elif valinta == "b":
        icao_koodi = input("Anna icao-koodi: ")
        if icao_koodi in lentoasemat:
            print("Lentoaseman tiedot: " + lentoasemat[icao_koodi])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif valinta == "c":
        break
    else:
        print("Virheellinen valinta")
    print()
