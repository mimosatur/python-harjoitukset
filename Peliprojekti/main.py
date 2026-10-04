# Tämä on ohjelman päätiedosto

from peli import Huone, Pelaaja, Esine, Apufunktiot
import json

# Luodaan muutama esine
esine1 = Esine("Kivi", 0.5)
esine2 = Esine("Oksa", 3.5)

# Luodaan huone
metsan_reuna = Huone("Metsän reuna")
aukio = Huone("Aukio")
lampi = Huone("Lampi")
portti = Huone("Portti")


# Lisätään esineitä huoneisiin
aukio.lisaa_esine(esine1)
aukio.lisaa_esine(esine2)




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
        print(f"Olet saapunut: {pelaaja.sijainti.nimi}")  
        pelaaja.sijainti.metsan_reuna()   
        suunta = input("Valitse mihin suuntaan haluat mennä: ")
        suunta = suunta.lower()

        if suunta == "itä":
            # suunnan itä polku
            print("Valitsit suunnan itä")
            print("--------------")

            ita1 = aukio
            pelaaja.liikkuu(ita1)
            print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
            #pelaaja.sijainti.tulosta_sisalto()
            pelaaja.sijainti.aukio()

            print("--------------")
            print("Edessäsi tie haarautuu oikealle ja vasemmalle")

            while True:

                suunta1 = input("Valitse kumpaan suuntaan haluat mennä (o vai v): ")
            
                if suunta1 == "o":
                    uusi_huone2 = lampi
                    pelaaja.liikkuu(uusi_huone2)
                    print("Valitsit suunnan oikea")
                    print("--------------")
                    print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
                    pelaaja.sijainti.lampi()
                    print("--------------")
                    print("Lammen rannalta lähtee polku pohjoiseen")
                    print("seurataksesi polkua syötä: pohjoinen")

                    while True:

                        seuraa = input("Anna komento: ")

                        if seuraa == "pohjoinen":
                            suunta2 = portti
                            pelaaja.liikkuu(suunta2)
                            print("Valitsit suunnan pohjoinen")
                            print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
                            pelaaja.sijainti.portti()

                        else:
                            Apufunktiot.virhe()
                        break

                elif suunta1 == "v":
                    print("Valitsit suunnan vasen")
                    print("--------------")
                    break
                else:
                    Apufunktiot.virhe()


        elif suunta == "pohjoinen": # suunnan pohjoinen polku
            print("Valitsit suunnan pohjoinen")
            print("--------------")
            pohjoinen1 = lampi
            pelaaja.liikkuu(pohjoinen1)
            print(f"Olet saapunut: {pelaaja.sijainti.nimi}")
            pelaaja.sijainti.lampi()
            print("--------------")
            print("Lammen reunalta lähtee tie koilliseen")
            print("Seurataksesi polkua syötä: koillinen")
           
            while True:

                pohjoinen2 = input("Anna komento: ")

                if pohjoinen2 == "koillinen":
                    print("Valitsit suunnan koillinen")
                    print("--------------")
                    koillinen = aukio
                    pelaaja.liikkuu(koillinen)
                    print(f"Olet saapunut: {pelaaja.sijainti.nimi}")
                    pelaaja.sijainti.aukio()
                    print("--------------")

                else:
                    Apufunktiot.virhe()
            

        elif suunta == "länsi": # suunnan länsi polku

            print("Valitsit suunnan länsi")
            print("----------")

            Apufunktiot.suunta_lansi()

    elif valinta == 2:  # Tästä pääsee jatkamaan käynnissä olevaa peliä
        
        print("Asetukset\n")            
        print()

    elif valinta == 3:  # Jos et haluakkaan pelata
        
        print("Lopetit pelin")
        