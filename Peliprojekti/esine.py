# Esine luokan luonti
class Esine:

    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = float(paino)

    def tulosta_esine(self):
        print(f"{self.nimi}, painaa {self.paino} kg.")


