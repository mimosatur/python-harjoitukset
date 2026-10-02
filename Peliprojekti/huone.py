
# tämä riippuu luokasta esine

class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.sisalto = []

    def lisaa_esine(self, esine):
        self.sisalto.append(esine)

    def tulosta_sisalto(self):
        print(f"Huoneen {self.nimi} sisältö: ")
        for esine in range(self.sisalto):
            esine = self.sisalto
            print(f"Esiineen nimi: {esine.nimi}, esineen paino: {self.paino} kg")



