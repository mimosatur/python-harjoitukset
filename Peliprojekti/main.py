# Tämä on ohjelman päätiedosto

from peli import Huone, Pelaaja, Esine, Apufunktiot
import json
#valinta = valinta[0].lower()

# Luodaan muutama esine
esine1 = Esine("Kivi", 0.5)
esine2 = Esine("Oksa", 3.5)

# Luodaan huone
metsan_reuna = Huone("Metsän reuna")
aukio = Huone("Aukio")
lampi = Huone("Lampi")


# Lisätään esineitä huoneisiin
aukio.lisaa_esine(esine1)
aukio.lisaa_esine(esine2)

huoneet = [metsan_reuna, aukio, lampi]




# Peli alkaa
ika = int(input("Kuinka vanha olet: "))

if ika < 12:
    print("Olet alaikäinen")


else:
    print(f"Tervetuloa Aamuruskon lehto peliin!")
    nimi = input("Mikä on pelaajanimesi?: ")

    # Tallenna pelaajan tiedot
    # luodaan pelaaja
    pelaaja = Pelaaja(nimi, metsan_reuna)
    print(f"Hei {pelaaja.nimi}!")

    
    Apufunktiot.tulosta_paavalikko()
    valinta = int(input("Valitse mitä haluat tehdä: "))
    # haluanko while loopin?
    if valinta == 1: 
        print("Peli aloitettu")
        print("----------")
        # Tässä luetaan pelaajalle pelin esittelyteksti
        with open("peliprojekti/peli/introteksti.txt") as intro_file:
            print(intro_file.read())
        print("--------------")
        # tähän ohjeet
        print(f"Olet nyt: {pelaaja.sijainti.nimi}")
        pelaaja.sijainti.tulosta_sisalto()
        suunta = input("Valitse mihin suuntaan haluat mennä: ")
        suunta = suunta.lower()

        if suunta == "itä":
            # suunnan itä polku
            print("Valitsit suunnan itä")
            print("--------------")
            
           
            input("Minne haluat mennä seuraavaksi: ")


        elif suunta == "pohjoinen":
            print("Valitsit suunnan pohjoinen")
            
            # suunnan pohjoinen polku

        elif suunta == "länsi": # suunnan länsi polku
            print("Valitsit suunnan länsi")
            print("----------")
            Apufunktiot.suunta_lansi()

    elif valinta == 2:  # Tästä pääsee jatkamaan käynnissä olevaa peliä
        
        print("Asetukset\n")            
        print()

    elif valinta == 3:  # Jos et haluakkaan pelata
        
        print("Lopetit pelin")
        