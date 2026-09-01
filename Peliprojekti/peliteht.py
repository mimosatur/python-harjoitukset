

nimi = input("Mikä on nimesi: ")
ika = int(input("Mikä on ikäsi: "))

while ika < 12:
    print("Olet alaikäinen")
    ika = int("Anna ikäsi uudelleen: ")
    if ika > 12:
        print(f"Tervetuloa peliini {nimi}!")



