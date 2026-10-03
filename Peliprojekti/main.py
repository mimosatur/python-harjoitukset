# Tämä on ohjelman päätiedosto
from peli import Huone, Pelaaja, Esine, Apufunktiot
#valinta = valinta[0].lower()

# luodaan huone
eteinen = Huone("Eteinen")

# luodaan muutama esine
esine1 = Esine("Kivi", 0.5)
esine2 = Esine("Oksa", 3.5)








# Peli alkaa
ika = int(input("Kuinka vanha olet: "))

if ika < 12:
    print("Olet alaikäinen")


else:
    print(f"Tervetuloa Aamuruskon lehto peliin!")
    nimi = input("Mikä on pelaajanimesi?: ")
    # Tallenna pelaajan tiedot
    # luodaan pelaaja
    pelaaja = Pelaaja(nimi, "eteinen")
    print(f"Hei {Pelaaja.nimi}!")

    
    Apufunktiot.tulosta_paavalikko()
    valinta = int(input("Valitse mitä haluat tehdä: "))
    if valinta == 1: 
        print("Peli aloitettu")
        print("----------")
        # Tähän pelin alkuteksti
        Apufunktiot.suunnan_valinta()
        suunta = input("Valitse mihin suuntaan haluat mennä: ")
        if suunta == "itä":
            # suunnan itä polku
            print("Valitsit suunnan itä")
        elif suunta == "pohjoinen":
            print("Valitsit suunnan pohjoinen")
            # suunnan pohjoinen polku
        elif suunta == "länsi":
            print("Valitsit suunnan länsi")
            # suunnan länsi polku
    elif valinta == 2:
        # Tästä pitäisi päästä jatkamaan käynnissä olevaa peliä
        print("Asetukset\n")            
        print()
    elif valinta == 3:
        # Jos et haluakkaan pelata
        print("Lopetit pelin")
        