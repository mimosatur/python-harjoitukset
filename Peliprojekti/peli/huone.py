
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

    def aukio(self):
            for esine in range(self.sisalto):
                esine = self.sisalto
                print(f"Esiineen nimi: {esine.nimi}, esineen paino: {self.paino} kg")
                print("Saavuit aukiolle josta on kaadettu kaikki puut")
                print("Maa on myös myllätty")
                print("Löydät maasta pussin")
                print("Sen sisältä löytyy 3 kpl puiden siemeniä")

    def lampi(self):
        print("Saavuit lammelle")

