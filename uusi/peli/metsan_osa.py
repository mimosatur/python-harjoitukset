
class MetsanOsa:
    def __init__(self, nimi):
        self.nimi = nimi
        self.roskat = []

    def lisaa_roska(self, roska):
        self.roskat.append(roska)

    def tulosta_roskat(self):
        if len(self.roskat) == 0:
            print("Olet kerännyt kaikki roskat tästä metsän osasta!")
        else:
            print(f"Metsän osan: {self.nimi} roskat:")
            for numero in range(len(self.roskat)):
                roska = self.roskat[numero]
                print(f"{numero + 1}. {roska.nimi} - {roska.kirjoittaja}")