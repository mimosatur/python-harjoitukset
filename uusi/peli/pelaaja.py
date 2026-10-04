# Pelaaja olion luonitia varten tehty luokka
class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.reppu = []
        self.sijainti = sijainti

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Siirryit paikkaan: {huone.nimi}")

    def keraa_roska(self, roska):
        self.reppu.append(roska)
        self.sijainti.roskat.remove(roska)
        print(f"Keräsit roskan: {roska.nimi}")

    def tulosta_keratyt_roskat(self):
        if len(self.keratyt_roskat) == 0:
            print("Et ole kerännyt vielä yhtään roskaa.")
        else:
            print("Keräämäsi roskat:")
            for roska in self.lainatut_kirjat:
                print(f"- {roska.nimi} - {roska.kirjoittaja}")