from .huone import Huone
from .esine import Esine

class Pelaaja:

    def __init__(self, nimi):
        self.reppu = []
        self.nimi = nimi
        self.sijainti = Huone()

    def liikkuu():
        pass

    def keraa_esine(self, tavarat):
        self.reppu.append(tavarat)



        