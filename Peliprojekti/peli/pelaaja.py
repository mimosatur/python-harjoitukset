
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



    def save_game(self):
        print("Tallennetaan peli.")
        try:
            with open("peliprojekti/peli/tallenna.txt", "w") as file:
                data = {"nimi": self.nimi, "sijainti": self.sijainti}
                json.dump(data, file)
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")

    def load_game(self):
        try:
            with open("peliprojekti/peli/tallenna.txt", "r") as file:
                data = json.load(file)
                #print("Ladattu tallennusdata:", data)
                self.nimi = data["nimi"]
                self.sijainti = data["sijainti"]
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")