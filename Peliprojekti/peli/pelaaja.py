
class Pelaaja:

    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.reppu = []
        self.sijainti = sijainti

    def liikkuu(self, huone):
        self.sijainti = huone
        print(f"Siirryit huoneeseen {huone.nimi}")

    def keraa_esine(self, esine):
        self.reppu.append(esine)
        print(f"Lisäsit tavaran {esine.nimi} reppuun")

    def tulosta_repun_sisalto(self):
        print("Repun sisältö: ")
        for esine in self.reppu:
            print(f"- {esine.nimi}, paino {esine.paino} kg")


