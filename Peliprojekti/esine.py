# Esine luokan luonti
class Esine:

    esineiden_lkm = 0

    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = float(paino)
        Esine.esineiden_lkm += 1

# Esimerkkiesineiden luonti
esineet = []
esine1 = Esine("Kivi", 1.5)
esine2 = Esine("Kirja", 2.5)
esine3 = Esine("Taikasauva", 0.5)
esine4 = Esine("Veitsi", 0.75)

esineet.append(esine1)
esineet.append(esine2)




