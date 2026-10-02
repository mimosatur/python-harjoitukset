

nimi = input("Mikä on nimesi: ")
ika = int(input("Kuinka vanha olet: "))


if ika < 12:
    print("Olet alaikäinen")

else:
    print(f"Tervetuloa Aamuruskon lehto peliin {nimi}!\n")
    
    
    while True:
        print("Päävalikko:\nAloita peli\nAsetukset\nLopeta")
        valinta = input("\nValitse mitä haluat tehdä: ")
        #valinta = valinta[0].lower()
        if valinta == "Aloita peli": 
            print("Peli aloitettu\n")
            inventaario()
        elif valinta == "Asetukset":
            print("Asetukset\n")
            tulosta()
            print()
        elif valinta == "Lopeta":
            print("Lopetit pelin")
            lopetus()
            break
    
        



