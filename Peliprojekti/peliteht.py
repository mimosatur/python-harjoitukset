

nimi = input("Mikä on nimesi: ")
ika = int(input("Mikä on ikäsi: "))

if ika < 12:
    print("Olet alaikäinen")
    ika = False

if ika > 12:
    print(f"Tervetuloa peliin {nimi}!")

print("Päävalikko:")

peli_käynnissä = True

