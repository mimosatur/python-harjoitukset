import json
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
        print(f"Lisäsit roskan {esine.nimi} reppuun")

    def tulosta_repun_sisalto(self):
        if len(self.reppu) == 0:
            print("Et ole kerännyt vielä yhtään roskaa")
        else:
            print("Repun sisältö: ")
            for esine in self.reppu:
                print(f"- {esine.nimi}")


    def tallenna_peli(self):
        print("Tallennetaan peli.")
        try:
            with open("peliprojekti/peli/save.txt", "w") as file:
                data = {"nimi": self.nimi, "sijainti": self.sijainti.nimi, "esineet": [esine.nimi for esine in self.reppu]}
                json.dump(data, file)
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")


    def lataa_peli(self):
        print("Ladataan peli")
        try:
            with open("peliprojekti/peli/save.txt", "r") as file:
                data = json.load(file)

            print("Tallennus löytyi!")
            print(data)
            self.nimi = data["nimi"]
            self.sijainti = data["sijainti"]
            self.reppu = data["esineet"]


        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")

