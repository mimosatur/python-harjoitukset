

nimi = input("Mikä on nimesi: ")
ika = int(input("Kuinka vanha olet: "))

reppu = []

def inventaario():
    esine = input("Anna esine: ")
    reppu.append(esine)
    return

def tulosta():
    return print(reppu)

def lopetus():
    return print("Nähdään ensikerralla!")

if ika < 12:
    print("Olet alaikäinen")

else:
    print(f"Tervetuloa Aamuruskon lehto peliin {nimi}!\n")
    
    
    while True:
        print("Päävalikko:\nAloita peli\nAsetukset\nLopeta")
        valinta = input("\nValitse mitä haluat tehdä: ")
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
    
        



