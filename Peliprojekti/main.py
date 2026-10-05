# Tämä on ohjelman päätiedosto
from peli import Huone, Pelaaja, Esine, Apufunktiot
import json

# Luodaan tarvittavat esineet
esine1 = Esine("Maitotölkki")
esine2 = Esine("Karkkipaperi")
esine3 = Esine("Tupakantumppi")
esine4 = Esine("Kertakäyttögrilli")
esine5 = Esine("Limsatölkki")
esine6 = Esine("Muovipussi")
esine7 = Esine("Autonrengas")

# Luodaan huoneet
metsan_reuna = Huone("Metsänreuna")
aukio = Huone("Aukio")
lampi = Huone("Lampi")
portti = Huone("Portti")

# Luodaan lista huoneista
huoneet = [metsan_reuna, aukio, lampi, portti]

# Lisätään esineet huoneisiin
metsan_reuna.lisaa_esine(esine1)
metsan_reuna.lisaa_esine(esine2)
metsan_reuna.lisaa_esine(esine3)
aukio.lisaa_esine(esine4)
aukio.lisaa_esine(esine5)
lampi.lisaa_esine(esine6)
lampi.lisaa_esine(esine7)



# Peli alkaa
ika = int(input("Kuinka vanha olet: "))

if ika < 12:
    print("Olet alaikäinen")


else:
    print(f"Tervetuloa Aamuruskon lehto peliin!")
    nimi = input("Mikä on pelaajanimesi?: ")

    # luodaan pelaaja
    pelaaja = Pelaaja(nimi, metsan_reuna)
    print(f"Hei {pelaaja.nimi}!")
    Pelaaja.tallenna_peli(pelaaja)

    
    Apufunktiot.tulosta_paavalikko()
    valinta = int(input("Valitse mitä haluat tehdä: "))
    
    if valinta == 1: 

        print("Peli aloitettu")
        print("----------")
        # Tässä luetaan pelaajalle pelin esittelyteksti
        with open("peliprojekti/peli/introteksti.txt") as intro_file:
            print(intro_file.read())
        print("--------------")

        # Tässä tulostetaan pelin ohjeet
        with open("peliprojekti/peli/ohjeet.txt") as ohjeet_file:
            print(ohjeet_file.read())

        print("--------------")  
        print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
        print("--------------")
        print("Kerää metsänreunassa olevat roskat")

        while True:

            keraa1 = Apufunktiot.keraa_roska(pelaaja.sijainti)
            if keraa1 is not None:
                pelaaja.keraa_esine(keraa1)
            print()

            keraa2 = Apufunktiot.keraa_roska(pelaaja.sijainti)
            if keraa2 is not None:
                pelaaja.keraa_esine(keraa2)
            print()

            keraa3 = Apufunktiot.keraa_roska(pelaaja.sijainti)
            if keraa3 is not None:
                pelaaja.keraa_esine(keraa3)

            if len(pelaaja.sijainti.esineet) == 0:
                break 
        print()
        pelaaja.tulosta_repun_sisalto()
        print("--------------")
        pelaaja.sijainti.metsan_reuna()
        print("--------------")   
        suunta = input("Valitse mihin suuntaan haluat mennä (L, P vai I): ")
        suunta = suunta.upper()

        if suunta == "I": # suunnan itä polku
            print("Valitsit suunnan itä")
            print("--------------")

            ita1 = aukio
            pelaaja.liikkuu(ita1)
            print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
            print("--------------")
            pelaaja.sijainti.tulosta_sisalto()
            print()
            pelaaja.sijainti.aukio()
            print()
            print("Tehtävän suorittamisesta ansaitsit seuraavat tavarat: ")
            pelaaja.keraa_esine(esine4)
            pelaaja.keraa_esine(esine5)
            print("--------------")
            print("Edessäsi tie haarautuu oikealle ja vasemmalle")

            while True:

                suunta1 = input("Valitse kumpaan suuntaan haluat mennä (O vai V): ")
                suunta1 = suunta1.upper()
            
                if suunta1 == "O":
                    print("Valitsit suunnan oikea")
                    print("--------------")
                    uusi_huone2 = lampi
                    pelaaja.liikkuu(uusi_huone2)
                    print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")

                    pelaaja.sijainti.tulosta_sisalto()
                    print("--------------")
                    pelaaja.sijainti.lampi()
                    print("--------------")
                    print("Tehtävän suorittamisesta ansaitsit seuraavat tavarat: ")
                    pelaaja.keraa_esine(esine6)
                    pelaaja.keraa_esine(esine7)
                    print("--------------")

                    print("Lammen rannalta lähtee polku pohjoiseen")
                    print("seurataksesi polkua syötä: pohjoinen")

                    while True:

                        seuraa = input("Anna komento: ")
                        seuraa = seuraa.lower()

                        if seuraa == "pohjoinen":
                            suunta2 = portti
                            pelaaja.liikkuu(suunta2)
                            print("Valitsit suunnan pohjoinen")
                            print("--------------")
                            print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
                            print("--------------")
                            pelaaja.sijainti.portti()
                            print("Olet kerännyt seuraavat tavarat:")
                            pelaaja.tulosta_repun_sisalto()
                            print("Peli loppui :)")                            
                            break
                        else:
                            Apufunktiot.virhe()
                        
                    break

                elif suunta1 == "V":
                    print("Valitsit suunnan vasen")
                    print("--------------")
                    suunta3 = portti
                    pelaaja.liikkuu(suunta3)
                    print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
                    pelaaja.sijainti.portti()
                    print("--------------")
                    print("Pelissä keräämäsi tavarat:")
                    pelaaja.tulosta_repun_sisalto()
                    print("Peli loppui :)")

                    break

                else:
                    Apufunktiot.virhe()


        elif suunta == "P": # suunnan pohjoinen polku
            print("Valitsit suunnan pohjoinen")
            print("--------------")
            pohjoinen1 = lampi
            pelaaja.liikkuu(pohjoinen1)
            print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
            print("--------------")
            pelaaja.sijainti.tulosta_sisalto()
            print("--------------")
            pelaaja.sijainti.lampi()
            print("--------------")
            print("Tehtävän suorittamisesta ansaitsit seuraavat tavarat: ")
            pelaaja.keraa_esine(esine6)
            pelaaja.keraa_esine(esine7)
            print("--------------")
            print("Lammen reunalta lähtee tie koilliseen")
            print("Seurataksesi tietä syötä: koillinen")
           
            while True:

                pohjoinen2 = input("Anna komento: ")
                pohjoinen2 = pohjoinen2.lower()

                if pohjoinen2 == "koillinen":
                    print("Valitsit suunnan koillinen")
                    print("--------------")
                    koillinen = aukio
                    pelaaja.liikkuu(koillinen)
                    print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
                    pelaaja.sijainti.tulosta_sisalto()
                    print("--------------")
                    pelaaja.sijainti.aukio()
                    print("--------------")
                    print("Tehtävän suorittamisesta ansaitsit seuraavat tavarat:")
                    pelaaja.keraa_esine(esine4)
                    pelaaja.keraa_esine(esine5)
                    print("--------------")
                    print("Aukion laidalta lähtee polku länteen")
                    print("Seurataksesi polkua syötä: länsi")
                 

                    while True:

                        lansi = input("Anna komento: ")

                        if lansi == "länsi":
                            print("Valitsit suunnan länsi")
                            print("--------------")
                            lansi2 = portti
                            pelaaja.liikkuu(lansi2)
                            print(f"Olet saapunut paikkaan: {pelaaja.sijainti.nimi}")
                            pelaaja.sijainti.portti()
                            print("Olet kerännyt seuraavat tavarat:")
                            pelaaja.tulosta_repun_sisalto()
                            print("Peli loppui :)")
                            break
                        else:
                            Apufunktiot.virhe() 
                    break

                else:
                    Apufunktiot.virhe()
            

        elif suunta == "L": # suunnan länsi polku

            print("Valitsit suunnan länsi")
            print("----------")

            Apufunktiot.suunta_lansi()

    elif valinta == 2:  # Tästä pääsee jatkamaan käynnissä olevaa peliä
        
        print("Jatketaan peliä")  # En saanut tallennusta toimimaan joten sitä ei nyt ole tässä

        print()

    elif valinta == 3:  # Jos et haluakkaan pelata
        
        print("Lopetit pelin")
        