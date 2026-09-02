

nimi = input("Mikä on nimesi: ")
ika = int(input("Kuinka vanha olet: "))

if ika < 12:
    print("Olet alaikäinen")

else:
    print(f"Tervetuloa peliin {nimi}!\n")
    
    peli_käynnissä = True
    while peli_käynnissä:
        print("Päävalikko:\nAloita peli\nAsetukset\nLopeta")
        valinta = input("\nValitse mitä haluat tehdä: ")
    if valinta == "Aloita peli":
        print("Peli aloitettu\n")
    elif valinta == "Asetukset":
        print("Asetukset\n")
    elif valinta == "Lopeta":
        print("Lopetit pelin")
        peli_käynnissä = False


