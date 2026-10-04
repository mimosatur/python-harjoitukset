# Tällä luokalla luodaan pelissä esiintyvät roskat

class Roska:

    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = float(paino)

    def tulosta_roska(self):
        print(f"roska: {self.nimi} painaa: {self.paino} kg verran")