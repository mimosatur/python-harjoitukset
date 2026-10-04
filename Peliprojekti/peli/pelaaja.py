
class Pelaaja:

    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.reppu = []
        self.sijainti = sijainti

    def liikkuu(self, huone):
        self.sijainti = huone

    def keraa_esine(self, esine):
        self.reppu.append(esine)
        self.sijainti.esineet.remove(esine)
        print(f"Lisäsit tavaran {esine.nimi} reppuun")

    def tulosta_repun_sisalto(self):
        if len(self.reppu) == 0:
            print("E_repun_sisaltot ole kerännyt vielä yhtään roskaa")
        else:
            print("Repun sisältö: ")
            for esine in self.reppu:
                print(f"- {esine.nimi}, paino {esine.paino} kg")


