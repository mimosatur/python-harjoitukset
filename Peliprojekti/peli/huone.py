
# tämä riippuu luokasta esine

class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.esineet = []

    # Lisää luodun esineen huoneeseen
    def lisaa_esine(self, esine):
        self.esineet.append(esine)

    # Tulostaa huoneen sisällön
    def tulosta_sisalto(self):
        if len(self.esineet) == 0:
            print("Huoneessa ei ole enää roskia")
        else:
            print(f"Paikan {self.nimi} sisältö: ")
            for numero in range(len(self.esineet)):
                esine = self.esineet[numero]
                print(f"{numero + 1}. {esine.nimi}")

    # Tehtävä aukio
    def aukio(self):
            print("Saavuit aukiolle josta on kaadettu kaikki puut")
            print("Maa on myös myllätty")
            print("----------")
            print("Näet aukean laidalla ilkeitä olioita kaatamassa puita")
            print("Tehtävänäsi on saada heidät lopettamaan puiden kaato")
            print("Lähestyt ilkeitä olioita ja sanot:\nHei, teidän pitää lopettaa puiden kaataminen!")
            print("Ilkeät oliot: 'Suostumme lopettamaan puiden kaatamisen jos arvaat oikein arvoituksemme'\n")
            print("----------")
            print("~~ Mikä menee ylös ja alas, mutta ei liiku yhtään? ~~")
            print("Vastaus vaihtoehdot:\nA Pilvi\nB Portaat\nC Tie")
            valinta = input("Anna vastauksesi: ")
            valinta = valinta.upper()

            while True:

                if valinta != "B":
                    valinta = input("Vastasit väärin.\nYritä uudelleen: ")
                    valinta = valinta.upper()
                elif valinta == "B":
                    print("Hienoa, arvasit oikein!")
                    print("Ilkeät oliot nyökkäävät hyväksymisen merkiksi, nousevat koneisiinsa ja ajavat pois")
                break

            return

    # Tehtävä lampi
    def lampi(self):
        print("Sen pinnalla kelluu paljon roskia")
        # kerää listaan roskia ja kun lista täynnä sano että valmista
        print("Tehtäväsi:")
        print("Kerää kaikki roskat lammesta (4 kpl)")
        print("Kerätäksesi roska syötä komento: kerää")

        roskat = []

        while len(roskat) < 4:
            
            komento = str(input("Anna komento> "))
            komento = komento.lower() # atm hyväksyy kaikki sanat 
            if komento == "kerää":
                roskat.append(komento)

            elif komento != "kerää":
                print("Virheellinen komento.")
                       
            elif len(roskat) == 4:
                print("Hienoa keräsit kaikki roskat")
                break

        return

    # Lopetus teksti
    def portti(self):
        print("Sinua vastaan kävelee metsänhoitaja")
        print("Hän pysähtyy kohdallesi ja sanoo:")
        print("Hienoa, olet suorittanut kaikki tehtävät.")
        print("Kiitos avustasi Aamuruskon lehdon entisöinnissä!")

    # Ensimmäisen suunnan valinta
    def metsan_reuna(self):
        print("Edessäsi on kolmen eri polkua: itä, pohjoinen ja länsi")
        print("Mitä pitkin haluaisit lähteä auttamaan metsän jälleenrakennuksessa?") 

