from peli import Huone, Pelaaja, Esine

nimi = input("Mikä on nimesi: ")
ika = int(input("Kuinka vanha olet: "))

# luodaan huone
eteinen = Huone("Eteinen")

# luodaan muutama esine
esine1 = Esine("Kivi", 0.5)
esine2 = Esine("Oksa", 3.5)

# luodaan pelaaja
pelaaja = Pelaaja(nimi, "eteinen")
print(f"Hei {pelaaja.nimi}!")

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
        elif valinta == "Asetukset":
            print("Asetukset\n")
            print()
        elif valinta == "Lopeta":
            print("Lopetit pelin")
            break
    
        



